<script lang="ts">
  export let error: boolean
  export let errorMessage: string
  export let success: boolean
  export let successMessage: string
</script>

{#if error}
  <div class="flex justify-center">
    <div class="pt-5 max-w-md">
      <div class="alert alert-error">
        <div class="flex-1">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            class="w-6 h-6 mx-2 stroke-current"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M18.364 18.364A9 9 0 005.636 5.636m12.728 12.728A9 9 0 015.636 5.636m12.728 12.728L5.636 5.636"
            />
          </svg>
          <!-- svelte-ignore a11y-label-has-associated-control -->
          <label id="errorLabel">{errorMessage}</label>
        </div>
      </div>
    </div>
  </div>
{:else if success}
  <!-- Center my tailwind div -->
  <div class="flex justify-center">
    <div class="pt-5 max-w-md ">
      <div class="alert alert-success">
        <div class="flex-1">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            class="w-6 h-6 mx-2 stroke-current"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
          <!-- svelte-ignore a11y-label-has-associated-control -->
          <label>{successMessage}</label>
        </div>
      </div>
    </div>
  </div>
{/if}
