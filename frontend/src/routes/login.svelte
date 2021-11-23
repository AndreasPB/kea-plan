<script lang="ts">
  let username = ""
  let password = ""

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
      alert("hooray you signed in")
    } else {
      alert("lol failed to login")
    }
  }
</script>

<div class="p-10 card bg-base-200">
  <div class="form-control">
    <label class="label">
      <span class="label-text">Username</span>
    </label>
    <input
      type="text"
      placeholder="username"
      class="input"
      bind:value={username}
    />
    <label class="label">
      <span class="label-text">Password</span>
    </label>
    <input
      type="text"
      placeholder="password"
      class="input"
      bind:value={password}
    />
  </div>
  <div class="flex justify-center pt-5">
    {#if username && password}
      <button class="btn btn-primary" on:click={signIn}>Sign in</button>
    {:else}
      <button class="btn btn-primary" disabled={true}>Sign in</button>
    {/if}
  </div>
</div>
