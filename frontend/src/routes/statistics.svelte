<script lang="ts">
  import StudentStatisticsTable from "../components/student-statistics-table.svelte"
  import TeacherStatisticsTable from "../components/teacher-statistics-table.svelte"
  import { user } from "../stores/auth.ts"
  import { onMount } from "svelte"

  // TODO: Should be held as an environment variable
  const API_URL = "http://localhost:2000"

  const fetchStatistics = async () => {
    switch ($user.userType) {
      case "student":
        var studentResponse = await fetch(
          `${API_URL}/statistics/student/${$user.personId}`
        )
        return await studentResponse.json()

      case "teacher":
        var teacherResponse = await fetch(
          `${API_URL}/statistics/semester/${$user.classId}`
        )
        return await teacherResponse.json()

      case "admin":
        throw new Error("Admin not yet implemented")

      default:
        throw new Error("Invalid user type")
    }
  }

  onMount(() => {
    if (!$user.accessToken) {
      location.href = "/login"
    }
  })
</script>

{#await fetchStatistics()}
  <h2>Loading statistics...</h2>
{:then statistics}
  <h1>Welcome to attendance statistics for {statistics.name}</h1>
  <br />

  {#if $user.user_type === "student"}
    <StudentStatisticsTable {statistics} />
  {:else if $user.user_type === "teacher"}
    <TeacherStatisticsTable {statistics} />
  {/if}
{/await}
