<script lang="ts">
  let username = ""
  let password = ""
  let error = false
  let success = false

  const signIn = async () => {
    let loginStatus = ""

    const payload = `username=${username}&password=${password}`

    await fetch("http://localhost:2000/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: payload,
    })
      .then((response) => response.json())
      .then((data) => (loginStatus = data.status))

    if (loginStatus === "success") {
      error = false
      success = true
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
  }
</script>

<div class="p-10 card bg-base-200">
  <form on:submit|preventDefault={signIn}>
    <div class="form-control">
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
{#if error}
  <div class="pt-5">
    <div class="alert alert-error">
      <div class="flex-1">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          class="w-6 h-6 mx-2 stroke-current"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636"
          />
        </svg>
        <label id="errorLabel">Incorrect username or password</label>
      </div>
    </div>
  </div>
{:else if success}
  <div class="pt-5">
    <div class="alert alert-success">
      <div class="flex-1">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          class="w-6 h-6 mx-2 stroke-current"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
        <label>Hooray you signed in!</label>
      </div>
    </div>
  </div>
{/if}
