<script lang="ts">
  import StudentStatisticsTable from "../components/student-statistics-table.svelte"
  import TeacherStatisticsTable from "../components/teacher-statistics-table.svelte"

  // TODO: Should be controlled by token/auth system
  const HARDCODED_ID = 1
  const HARDCODED_CLASS_ID = 1
  const HARDCODED_USER_TYPE = "teacher"

  // TODO: Should be held as an environment variable
  const API_URL = "http://localhost:2000"

  const fetchStatistics = async () => {
    switch (HARDCODED_USER_TYPE) {
      case "student":
        var studentResponse = await fetch(
          `${API_URL}/statistics/student/${HARDCODED_ID}`
        )
        return await studentResponse.json()

      case "teacher":
        var teacherResponse = await fetch(
          `${API_URL}/statistics/semester/${HARDCODED_CLASS_ID}`
        )
        return await teacherResponse.json()

      case "admin":
        throw new Error("Admin not yet implemented")

      default:
        throw new Error("Invalid user type")
    }
  }
</script>

{#await fetchStatistics()}
  <h2>Loading statistics...</h2>
{:then statistics}
  <h1>Welcome to attendance statistics for {statistics.name}</h1>
  <br />

  {#if HARDCODED_USER_TYPE === "student"}
    <StudentStatisticsTable {statistics} />
  {/if}
  {#if HARDCODED_USER_TYPE === "teacher"}
    <TeacherStatisticsTable {statistics} />
  {/if}
{/await}
