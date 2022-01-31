<script>
  import DynamicForm from "../components/dynamic-form.svelte"
</script>

<h1>Admin</h1>

TODO: Control the data for the form here

<DynamicForm
  data={{
    id: 42,
    name: "John Doe",
  }}
  endpoint="/student"
  formMethod="POST"
/>
