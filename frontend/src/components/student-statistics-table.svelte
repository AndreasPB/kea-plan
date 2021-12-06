<script lang="ts">
  export let statistics
</script>

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
