<script lang="ts">
  export let statistics
  let chosenCourse
</script>

<h2>Class courses:{chosenCourse}</h2>
<div class="btn-group">
{#each statistics.courses as course, index}
  <input type="radio" name="options" bind:value={chosenCourse} id="option1" checked="checked" data-title="{course.name}{index}" data-value="{index}" class="btn"> 
{/each}
</div>

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
