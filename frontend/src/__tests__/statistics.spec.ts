import "@testing-library/jest-dom"

import { render } from "@testing-library/svelte"

import Statistics from "../routes/statistics.svelte"
import StudentStatisticsTable from "../components/student-statistics-table.svelte"
import LecturerStatisticsTable from "../components/lecturer-statistics-table.svelte"

const studentTableData = {
  id: 1,
  name: "John",
  courses: [
    {
      id: 1,
      name: "Math",
      attendance_percentage: 90,
    },
    {
      id: 2,
      name: "English",
      attendance_percentage: 80,
    },
    {
      id: 3,
      name: "Physics",
      attendance_percentage: 70,
    },
  ],
}

const lecturerTableData = {
  id: 1,
  name: "Class 1",
  courses: [
    {
      id: 1,
      name: "Math",
      course_attendance: [
        {
          name: "John",
          attendance_percentage: 90,
        },
        {
          name: "Jane",
          attendance_percentage: 95,
        },
      ],
    },
    {
      id: 2,
      name: "English",
      course_attendance: [
        {
          name: "John",
          attendance_percentage: 80,
        },
        {
          name: "Jane",
          attendance_percentage: 85,
        },
      ],
    },
    {
      id: 3,
      name: "Physics",
      course_attendance: [
        {
          name: "John",
          attendance_percentage: 70,
        },
        {
          name: "Jane",
          attendance_percentage: 75,
        },
      ],
    },
  ],
}

describe("Statistics", () => {
  it("should render", async () => {
    const page = render(Statistics)

    expect(page)
    expect(page.getByText("Loading statistics..."))
  })

  it("should build a table with student data", async () => {
    const table = render(StudentStatisticsTable, {
      statistics: studentTableData,
    })

    expect(table)
    expect(table.getAllByText("Name"))
    expect(table.getAllByText("Math"))
    expect(table.getByText("Attendance"))
    expect(table.getByText("90%"))
  })

  it("should build a table with lecturer/semester data", async () => {
    const { getByText, getAllByText, queryByText } = render(
      LecturerStatisticsTable,
      {
        statistics: lecturerTableData,
      }
    )

    // Start class index 0(Math)
    expect(getAllByText("Name"))
    expect(getAllByText("Attendance"))
    expect(getAllByText("John"))
    expect(getByText("90%"))
    expect(getAllByText("Jane"))
    expect(getByText("95%"))

    expect(queryByText("80%")).toBeNull()
  })

  it("should be able to build different tables dependant on the radio options", async () => {
    const { getByText, getAllByText, queryByText } = render(
      LecturerStatisticsTable,
      {
        statistics: lecturerTableData,
        chosenCourse: "English",
      }
    )

    expect(getAllByText("Name"))
    expect(getAllByText("Attendance"))
    expect(getAllByText("John"))
    expect(getByText("80%"))
    expect(getAllByText("Jane"))
    expect(getByText("85%"))

    expect(queryByText("90%")).toBeNull()
  })
})
