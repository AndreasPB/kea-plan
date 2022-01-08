<script lang="ts">
  import { user } from "../stores/auth"
  import { onMount } from "svelte"
  import SuccessErrorMessage from "../components/success-error-message.svelte"

  let username = ""
  let password = ""
  let error = false
  let success = false

  const signIn = async () => {
    const payload = `username=${username}&password=${password}`

    await fetch("http://localhost:2000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: payload,
    }).then(function (response) {
      if (response.status === 200) {
        error = false
        success = true
        response.json().then((data) => {
          $user.username = data.username
          $user.full_name = data.full_name
          $user.access_token = data.access_token
          $user.user_type = data.user_type
          $user.student_id = data.student_id
          $user.lecturer_id = data.lecturer_id
          $user.class_id = data.class_id
        })
        setTimeout(function () {
          window.location.href = "/"
        }, 250)
      } else {
        error = true
        password = ""
        setTimeout(function () {
          error = false
        }, 2500)
      }
    })
  }

  onMount(() => {
    if ($user.access_token) {
      location.href = "/"
    }
  })
</script>

<div class="p-10 card bg-base-200">
  <form on:submit|preventDefault={signIn}>
    <div class="form-control">
      <!-- svelte-ignore a11y-label-has-associated-control -->
      <label class="label">
        <span class="label-text">Username</span>
      </label>
      <input
        type="text"
        placeholder="username"
        class="input"
        id="username"
        bind:value={username}
      />
      <!-- svelte-ignore a11y-label-has-associated-control -->
      <label class="label">
        <span class="label-text">Password</span>
      </label>
      <input
        bind:value={password}
        type="password"
        placeholder="password"
        id="password"
        class="w-full input"
      />
    </div>
    <div class="flex justify-center pt-5">
      {#if username && password}
        <button class="btn btn-primary" id="signin" type="submit"
          >Sign in</button
        >
      {:else}
        <button class="btn btn-primary" id="signin" disabled={true}
          >Sign in</button
        >
      {/if}
    </div>
  </form>
</div>
<SuccessErrorMessage
  {success}
  successMessage="Hooray you signed in!"
  {error}
  errorMessage="Incorrect username or password"
/>
