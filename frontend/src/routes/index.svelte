<script lang="ts">
  import { onMount } from "svelte"
  import { user } from "../stores/auth"

  let chosenCourse: string
  let token: any

  onMount(async () => {
    if (!$user.access_token) {
      location.href = "/login"
    }

    // const tokenResponse = await fetch(
    //   `http://localhost:2000/lesson/token/SDFD`
    // )

    // console.log(await tokenResponse.json())
  })

  const fetchToken = async () => {
    const tokenResponse = await fetch(`http://localhost:2000/token/generate`)
    token = await tokenResponse.json()
    try {
      postLesson(token)
    } catch (e) {
      console.error(e)
    }
  }

  const fetchCourses = async (courseId) => {
    const courseResponse = await fetch(
      `http://localhost:2000/studentclass_course/${courseId}`
    )
    return await courseResponse.json()
  }

  const postLesson = async (attendance_token: string) => {
    const res = await fetch("http://localhost:2000/lesson/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        start: Date.now(),
        duration: 180,
        attendance_token: attendance_token,
      }),
    })
    const json = await res.json()
    console.log(JSON.stringify(json))
    return JSON.stringify(json)
  }

  const postStudentAttendance = async () => {
    // 1. is token valid?
    const tokenResponse = await fetch(
      `http://localhost:2000/lesson/token/${token}`
    )

    const tokenJson = await tokenResponse.json()

    // 2. what lesson does the token belong to?
    const lessonId = tokenJson.id

    //3. create a attendance for the lesson
    const lessonResponse = await fetch(`http://localhost:2000/attendance`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        time_of_attendance: Date.now(),
        lesson_id: lessonId,
      }),
    })
    return await lessonResponse.json()
  }
</script>

<h1 class="flex justify-center m-10">Welcome to KEAPlan {$user.full_name}</h1>

{#if $user.user_type == "student"}
  <div class="flex justify-center">
    <div class="p-10 card bg-base-200 max-w-md">
      <form on:submit|preventDefault={postStudentAttendance}>
        <div class="form-control">
          <label class="label">
            <span class="label-text">Token</span>
          </label>
          <div class="flex space-x-2">
            <input
              type="text"
              placeholder="enter token"
              class="w-full input input-primary input-bordered"
              bind:value={token}
            />
            <button class="btn btn-primary">submit</button>
          </div>
        </div>
      </form>
    </div>
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
    <div class="flex justify-center btn-group mb-4">
      {#if chosenCourse}
        <button class="btn btn-primary" on:click={fetchToken}
          >Generate token</button
        >
      {:else}
        <h1>Please choose a course to generate attendance token</h1>
      {/if}
    </div>

    {#if token}
      <h1>{token}</h1>
    {/if}
  {/await}
{:else if $user.user_type == "admin"}
  <!-- else content here -->
  <h1>I AM ADMIN</h1>
{/if}
