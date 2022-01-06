<script lang="ts">
  import StudentStatisticsTable from "../components/student-statistics-table.svelte"
  import LecturerStatisticsTable from "../components/lecturer-statistics-table.svelte"
  import { user } from "../stores/auth"
  import { onMount } from "svelte"

  // TODO: Should be held as an environment variable
  const API_URL = "http://localhost:2000"

  const fetchStatistics = async () => {
    switch ($user.user_type) {
      case "student":
        var studentResponse = await fetch(
          `${API_URL}/statistics/student/${$user.person_id}`
        )
        return await studentResponse.json()

      case "lecturer":
        var lecturerResponse = await fetch(
          `${API_URL}/statistics/semester/${$user.class_id}`
        )
        return await lecturerResponse.json()

      case "admin":
        throw new Error("Admin not yet implemented")

      default:
        throw new Error("Invalid user type")
    }
  }

  onMount(() => {
    if (!$user.access_token) {
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
  {:else if $user.user_type === "lecturer"}
    <LecturerStatisticsTable {statistics} />
  {/if}
{/await}
