<script lang="ts">
  import { compute_rest_props } from "svelte/internal"

  // TODO: Should be controlled by token/auth system
  const HARDCODED_ID: number = 1
  const HARDCODED_CLASS_ID: number = 1
  const HARDCODED_USER_TYPE: string = "teacher"

  // TODO: Should be held as an environment variable
  const API_URL: string = "http://localhost:2000"

  const fetchStatistics = async () => {
    switch (HARDCODED_USER_TYPE) {
      case "student":
        const studentResponse = await fetch(
          `${API_URL}/statistics/student/${HARDCODED_ID}`
        )
        return await studentResponse.json()

      case "teacher":
        const teacherResponse = await fetch(
          `${API_URL}/statistics/semester/${HARDCODED_CLASS_ID}`
        )
        return await teacherResponse.json()

      case "admin":
        throw new Error("Admin not yet implemented")
    }
  }
</script>

{#await fetchStatistics()}
  <h2>Loading statistics...</h2>
{:then statistics}
  <h1>Welcome to attendance statistics for {statistics.name}</h1>
  <br />
  <!-- For student user type -->
  {#if HARDCODED_USER_TYPE === "student"}
    <h2>Your courses:</h2>

    <table class="table w-full">
      <thead>
        <tr>
          <th>Name</th>
          <th>Attendance</th>
        </tr>
      </thead>
      <tbody>
        {#each statistics.courses as course}
          <tr>
            <td>{course.name}</td>
            <td>{course.attendance_percentage}%</td>
          </tr>
        {/each}
      </tbody>
    </table>
  {/if}
  <!-- For teacher user type -->
  {#if HARDCODED_USER_TYPE === "teacher"}
    <h2>Class courses:</h2>

    {#each statistics.courses as course}
      <h1>{course.name}</h1>
      <table class="table w-full table-compact">
        <thead>
          <tr>
            <th>Name</th>
            <th>Attendance</th>
          </tr>
        </thead>
        <tbody>
          {#each course.course_attendance as attendance}
            <tr>
              <td>{attendance.name}</td>
              <td>{attendance.attendance_percentage}%</td>
            </tr>
          {/each}
        </tbody>
      </table>
    {/each}
  {/if}
{/await}
