<script lang="ts">
  export let token: string
  export let lessonAttendance

  const timeConverter = (time: Date) => {
    return new Date(time).toLocaleTimeString("en", {
      timeStyle: "short",
      hour12: false,
    })
  }
</script>

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
              <td>{timeConverter(attendance.Attendance.time_of_attendance)}</td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  {/if}
{/if}
