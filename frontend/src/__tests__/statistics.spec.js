import "@testing-library/dom"

import { render } from "@testing-library/svelte"

import Statistics from "../routes/statistics.svelte"
import StudentStatisticsTable from "../components/student-statistics-table.svelte"
import TeacherStatisticsTable from "../components/teacher-statistics-table.svelte"

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

const teacherTableData = {
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

    expect(page).toBeTruthy()
    expect(page.getByText("Loading statistics...")).toBeTruthy()
  })

  it("should build a table with student data", async () => {
    const table = render(StudentStatisticsTable, {
      statistics: studentTableData,
    })

    expect(table).toBeTruthy()
    expect(table.getAllByText("Math")).toBeTruthy()
  })

  it("should build a table with teacher/semester data", async () => {
    const table = render(TeacherStatisticsTable, {
      statistics: teacherTableData,
    })

    expect(table).toBeTruthy()
    expect(table.getAllByText("John")).toBeTruthy()
  })
})
