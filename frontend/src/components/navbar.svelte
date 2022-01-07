<script lang="ts">
  import { user } from "../stores/auth"
</script>

<div class="navbar mb-2 shadow-lg bg-neutral text-neutral-content">
  <div class="flex-1 px-2 mx-2 lg:flex">
    <a href="/">
      <span class="text-lg font-bold"> KEAPlan </span>
    </a>
  </div>
  <div class="flex-none">
    {#if $user.access_token}
      <div>
        <a class="btn btn-ghost btn-sm" href="/statistics"> Statistics </a>
      </div>
      <div class="dropdown dropdown-end">
        <div tabindex="0" class="m-1 btn">Menu</div>
        <ul
          tabindex="0"
          class="p-2 shadow menu dropdown-content bg-base-100 rounded-box w-52"
        >
          <li>
            <a class="navbar-item" href="/profile">
              <span class="icon">
                <i class="fas fa-user" />
              </span>
              Profile
            </a>
          </li>
          <li>
            <a class="navbar-item" href="/settings">
              <span class="icon">
                <i class="fas fa-cog" />
              </span>
              Settings
            </a>
          </li>
          <li>
            <a
              class="navbar-item"
              href="/login"
              on:click={() =>
                ($user = {
                  username: null,
                  full_name: null,
                  access_token: null,
                  user_type: null,
                  person_id: null,
                  class_id: null,
                })}
            >
              <span class="icon">
                <i class="fas fa-sign-out-alt" />
              </span>
              Sign out
            </a>
          </li>
        </ul>
      </div>
      <div class="avatar placeholder">
        <div
          class="bg-neutral-focus text-neutral-content rounded-full w-12 h-12"
        >
          <span class="text-3xl">{$user.full_name.charAt(0)}</span>
        </div>
      </div>
    {/if}
  </div>
</div>
