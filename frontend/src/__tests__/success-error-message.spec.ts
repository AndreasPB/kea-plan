import "@testing-library/jest-dom"

import { render } from "@testing-library/svelte"
import SuccessErrorMessage from "../components/success-error-message.svelte"

describe("Success and error message", () => {
  it("should display success message", () => {
    const { getByText, queryByText } = render(SuccessErrorMessage, {
      successMessage: "Success message",
      success: true,
      errorMessage: "Error message",
      error: false,
    })
    expect(getByText("Success message")).toBeInTheDocument()
    expect(queryByText("Error message")).not.toBeInTheDocument()
  })

  it("should display error message", () => {
    const { getByText, queryByText } = render(SuccessErrorMessage, {
      successMessage: "Success message",
      success: false,
      errorMessage: "Error message",
      error: true,
    })
    expect(getByText("Error message")).toBeInTheDocument()
    expect(queryByText("Success message")).not.toBeInTheDocument()
  })
})
