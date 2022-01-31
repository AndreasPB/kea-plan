<script lang="ts">
  export let data: {} = {
    name: "Darth Vader",
    age: 69,
  }
  export let endpoint: string
  export let formMethod: string = "POST"

  const baseUrl = "http://localhost:2000"

  const formAction = async () => {
    console.log("Woop woop - Form submitted")

    const response = await fetch(baseUrl + endpoint, {
      method: formMethod,
      body: JSON.stringify(data),
    })

    const json = await response.json()
    console.log(json)
  }

  const capitalizeFirstLetter = (s: string) => {
    return s.charAt(0).toUpperCase() + s.slice(1)
  }
</script>

<!-- TODO: Control the request from the component -->

<form on:submit|preventDefault={formAction}>
  <div class="form-control">
    <h1>endpoint: {endpoint}</h1>
    <h1>formMethod: {formMethod}</h1>
    <h1>data: {JSON.stringify(data)}</h1>
    {#each Object.entries(data) as [key, value]}
      <!-- svelte-ignore a11y-label-has-associated-control -->
      <label class="label">
        <span class="label-text">{capitalizeFirstLetter(key)}</span>
      </label>
      <input
        type="text"
        {value}
        placeholder={key}
        class="input input-bordered"
      />
    {/each}
  </div>
  <div class="flex justify-center pt-5">
    <button class="btn btn-primary" type="submit"
      >TODO: Should be dynamic(post/del/create)</button
    >
  </div>
</form>
