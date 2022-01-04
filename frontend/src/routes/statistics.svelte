<script lang="ts">
  import { variables } from "../variables"
  import StudentStatisticsTable from "../components/student-statistics-table.svelte"
  import TeacherStatisticsTable from "../components/teacher-statistics-table.svelte"

  // TODO: Should be controlled by token/auth system
  const HARDCODED_ID = 1
  const HARDCODED_CLASS_ID = 1
  let HARDCODED_USER_TYPE = "student"
  HARDCODED_USER_TYPE = "teacher"

  const fetchStatistics = async () => {
    switch (HARDCODED_USER_TYPE as any) {
      case "student":
        var studentResponse = await fetch(
          `${variables.apiPath}/statistics/student/${HARDCODED_ID}`
        )
        return await studentResponse.json()

      case "teacher":
        var teacherResponse = await fetch(
          `${variables.apiPath}/statistics/semester/${HARDCODED_CLASS_ID}`
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
  {:else if HARDCODED_USER_TYPE === "teacher"}
    <TeacherStatisticsTable {statistics} />
  {/if}
{/await}
