import { persist, sessionStorage } from "@macfja/svelte-persistent-store"
import { writable } from "svelte/store"

export const user = persist(
  writable({
    username: null,
    full_name: null,
    access_token: null,
    user_type: null,
    student_id: null,
    lecturer_id: null,
    class_id: null,
  }),
  sessionStorage(),
  "user"
)
