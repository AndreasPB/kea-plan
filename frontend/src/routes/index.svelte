<script lang="ts">
  import { onMount } from "svelte"
  import { user } from "../stores/auth"

  let chosenCourse: string
  let token: any

  onMount(() => {
    if (!$user.access_token) {
      location.href = "/login"
    }
  })

  const fetchToken = async () => {
    const tokenResponse = await fetch(`http://localhost:2000/token/generate`)
    token = await tokenResponse.json()
  }

  const fetchCourses = async (courseId) => {
    const courseResponse = await fetch(
      `http://localhost:2000/studentclass_course/${courseId}`
    )
    return await courseResponse.json()
  }
</script>

<h1>Welcome to KEAPlan</h1>

{#if $user.user_type == "student"}
  <!-- content here -->
  <div class="form-control">
    <label class="label">
      <span class="label-text">Token</span>
    </label>
    <input type="text" placeholder="username" class="input" />
  </div>
{:else if $user.user_type == "lecturer"}
  {#await fetchCourses($user.class_id)}
    <p>Loading courses...</p>
  {:then courses}
    <div class="flex justify-center btn-group mb-4">
      {#each courses as course}
        <input
          class="btn"
          type="radio"
          name="options"
          bind:group={chosenCourse}
          value={course.name}
          data-title={course.name}
        />
      {/each}
    </div>

    <button class="btn btn-primary" on:click={fetchToken}>Generate token</button
    >
    {#if token}
      <h1>{token}</h1>
    {/if}
  {/await}
{:else if $user.user_type == "admin"}
  <!-- else content here -->
  <h1>I AM ADMIN</h1>
{/if}
