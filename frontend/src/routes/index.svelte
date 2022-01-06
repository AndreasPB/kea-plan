<script lang="ts">
  import { onMount } from "svelte"
  import { user } from "../stores/auth"

  let lessonAttendance
  let chosenCourse: string
  let token: string
  let success = false
  let error = false

  onMount(async () => {
    if (!$user.access_token) {
      location.href = "/login"
    }
    console.log(success + " " + error)
  })

  const tableRefresher = async () => {
    console.log("Refreshing table-data every 5 seconds")

    while (token) {
      await new Promise((resolve) => setTimeout(resolve, 5000))
      await fetchAttendance()
    }
  }

  const fetchToken = async () => {
    const tokenResponse = await fetch(`http://localhost:2000/token/generate`)
    token = await tokenResponse.json()
    console.log(token)
    try {
      postLesson(token)
      await tableRefresher()
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
  const fetchLessonId = async (): Promise<number> => {
    // is token valid?
    const tokenResponse = await fetch(
      `http://localhost:2000/lesson/token/${token}`
    )

    // what lesson does the token belong to?
    return (await tokenResponse.json()).id
  }

  const postAttendance = async () => {
    const lessonId = await fetchLessonId()

    // create a attendance for the lesson
    const lessonResponse = await fetch(`http://localhost:2000/attendance`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        time_of_attendance: Date.now(),
        lesson_id: lessonId,
        student_id: $user.person_id,
      }),
    })
    if (lessonResponse.status === 200) {
      success = true
      setTimeout(() => {
        success = false
      }, 5000)
    } else {
      error = true
      setTimeout(() => {
        error = false
      }, 2500)
    }
    return await lessonResponse.json()
  }

  const fetchAttendance = async () => {
    const lessonId = await fetchLessonId()
    const attendanceResponse = await fetch(
      `http://localhost:2000/attendance/lesson/${lessonId}`
    )
    lessonAttendance = await attendanceResponse.json()
    console.log(lessonAttendance)
  }

  const timeConverter = (time: Date) => {
    return new Date(time).toLocaleTimeString("en", {
      timeStyle: "short",
      hour12: false,
    })
  }
</script>

<h1 class="flex justify-center m-10">Welcome to KEAPlan {$user.full_name}</h1>

{#if $user.user_type == "student"}
  <div class="flex justify-center">
    <div class="p-10 card bg-base-200 max-w-md">
      <form
        on:submit|preventDefault={async () => {
          if (token && token.length === 4 && !success && !error)
            await postAttendance()
        }}
      >
        <div class="form-control">
          <!-- svelte-ignore a11y-label-has-associated-control -->
          <label class="label">
            <span class="label-text">Token</span>
          </label>
          <div class="flex space-x-2">
            <input
              type="text"
              placeholder="enter token"
              class="w-full input input-primary input-bordered"
              maxlength="4"
              bind:value={token}
            />
            {#if token && token.length === 4 && !success && !error}
              <button class="btn btn-primary">submit</button>
            {:else}
              <button class="btn btn-primary" disabled> submit </button>
            {/if}
          </div>
        </div>
      </form>
    </div>
  </div>

  {#if error}
    <div class="flex justify-center">
      <div class="pt-5 max-w-md">
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
            <!-- svelte-ignore a11y-label-has-associated-control -->
            <label id="errorLabel">Unknown token</label>
          </div>
        </div>
      </div>
    </div>
  {:else if success}
    <!-- Center my tailwind div -->
    <div class="flex justify-center">
      <div class="pt-5 max-w-md ">
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
            <!-- svelte-ignore a11y-label-has-associated-control -->
            <label>Hooray you are registerd preset to the lesson!</label>
          </div>
        </div>
      </div>
    </div>
  {/if}
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
  {/await}

  {#if token}
    <div class="flex justify-center pt-5">
      <h1 class="mb-5 text-5xl font-bold">{token}</h1>
    </div>
    {#if lessonAttendance && lessonAttendance.length > 0}
      <div class="overflow-x-auto pt-5">
        <table class="table w-full">
          <thead>
            <tr>
              <th />
              <th>Name</th>
              <th>Attendance time</th>
            </tr>
          </thead>
          <tbody>
            <!-- For hver attendance der matcher lesson id for token -->
            {#each lessonAttendance as attendance}
              <tr>
                <td>{attendance.Attendance.student_id}</td>
                <td>{attendance.name}</td>
                <td
                  >{timeConverter(attendance.Attendance.time_of_attendance)}</td
                >
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    {/if}
  {/if}
{:else if $user.user_type == "admin"}
  <!-- else content here -->
  <h1>I AM ADMIN</h1>
{/if}
