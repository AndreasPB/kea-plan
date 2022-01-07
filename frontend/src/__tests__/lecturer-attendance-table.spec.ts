import "@testing-library/jest-dom"

import { render } from "@testing-library/svelte"
import LecturerAttendanceTable from "../components/lecturer-attendance-table.svelte"

const attendanceTableData = [
  {
    Attendance: {
      time_of_attendance: "2022-01-07T13:09:40.281000",
      lesson_id: 7,
      student_id: 1,
      id: 7,
    },
    name: "John Doe",
  },
  {
    Attendance: {
      time_of_attendance: "2022-01-07T13:19:40.281000",
      lesson_id: 7,
      student_id: 2,
      id: 8,
    },
    name: "Jake Smith",
  },
]

describe("Lecturer attendance table", () => {
  it("should display table", () => {
    const { getByText, queryByText } = render(LecturerAttendanceTable, {
      token: "ASDF",
      lessonAttendance: attendanceTableData,
    })

    expect(getByText("John Doe")).toBeInTheDocument()
    expect(getByText("Jake Smith")).toBeInTheDocument()
  })

  it("should not display table - missing attendance", () => {
    const { queryByText } = render(LecturerAttendanceTable, {
      token: "ASDF",
      lessonAttendance: [],
    })

    expect(queryByText("John Doe")).not.toBeInTheDocument()
    expect(queryByText("Jake Smith")).not.toBeInTheDocument()
  })

  it("should not display table - missing token", () => {
    const { queryByText } = render(LecturerAttendanceTable, {
      token: "",
      lessonAttendance: attendanceTableData,
    })

    expect(queryByText("John Doe")).not.toBeInTheDocument()
    expect(queryByText("Jake Smith")).not.toBeInTheDocument()
  })
})
