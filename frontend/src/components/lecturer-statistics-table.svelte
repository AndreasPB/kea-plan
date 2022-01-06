<script lang="ts">
  export let statistics
  export let chosenCourse = statistics.courses[0].name
</script>

<div class="flex justify-center btn-group mb-4">
  {#each statistics.courses as course}
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

{#each statistics.courses as course}
  {#if course.name == chosenCourse}
    <table class="table w-full table-compact flex justify-center">
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
  {/if}
{/each}
