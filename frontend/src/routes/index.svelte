<script lang="ts">
  import SuccessErrorMessage from "../components/success-error-message.svelte"
  import LecturerAttendanceTable from "../components/lecturer-attendance-table.svelte"
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

  const fetchCourses = async (classId: number) => {
    const courseResponse = await fetch(
      `http://localhost:2000/studentclass_course/${classId}`
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
        student_id: $user.student_id,
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
</script>

<h1 class="flex justify-center m-10">Welcome to KEAPlan {$user.full_name}</h1>

{#if $user.user_type === "student"}
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
  <SuccessErrorMessage
    {success}
    successMessage="Hooray you are registered present to the lesson!"
    {error}
    errorMessage="Unknown token"
  />
{:else if $user.user_type === "lecturer"}
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
  <LecturerAttendanceTable {token} {lessonAttendance} />
{:else if $user.user_type === "admin"}
  <!-- else content here -->
  <h1>I AM ADMIN</h1>
{/if}
