import React, { useState } from 'react';
import SearchBar from './SearchBar';
import IntakeFilter from './IntakeFilter';
import YearFilter from './YearFilter';
import CourseList from './CourseList';
import './CourseSchedule.css';

const CourseSchedule = () => {
  // State for managing selected filters
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedIntake, setSelectedIntake] = useState('');
  const [selectedYear, setSelectedYear] = useState('2024-2025');

  // Sample course data
  const courses = [
    { id: 1, name: 'Course 1', year: '2024-2025', intake: 'FALL' },
    { id: 2, name: 'Course 2', year: '2024-2025', intake: 'SPRING' },
    { id: 3, name: 'Course 3', year: '2023-2024', intake: 'FALL' },
  ];

  // Filter courses based on search term, selected intake, and year
  const filteredCourses = courses.filter(course => {
    const matchesSearch = course.name.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesIntake = selectedIntake === '' || course.intake.toLowerCase() === selectedIntake.toLowerCase();
    const matchesYear = course.year === selectedYear;
    return matchesSearch && matchesIntake && matchesYear;
  });

  return (
    <div className="course-schedule">
      <h1>Course Schedule</h1>

      <div className="filters-container">
        <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
        <IntakeFilter selectedIntake={selectedIntake} setSelectedIntake={setSelectedIntake} />
        <YearFilter selectedYear={selectedYear} setSelectedYear={setSelectedYear} />
      </div>

      <CourseList courses={filteredCourses} />
    </div>
  );
};

export default CourseSchedule;
