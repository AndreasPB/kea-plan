<script lang="ts">
  export let statistics
</script>

<h2>Class courses:</h2>

{#each statistics.courses as course}
  <h1 class="mt-2">{course.name}</h1>
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
