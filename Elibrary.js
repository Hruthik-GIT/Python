import React, { useState } from 'react';
import './ELibrary.css';

const ELibrary = () => {
  const [searchCriteria, setSearchCriteria] = useState('Title');
  const [searchWord, setSearchWord] = useState('');
  const [selectedCourse, setSelectedCourse] = useState('-Courses-');
  const [selectedDepartment, setSelectedDepartment] = useState('-Department-');

  const courses = ["Computer Science", "Mathematics", "Physics", "Engineering"];
  const departments = ["Computer Science", "Mathematics", "Physics", "Engineering"];

  const handleSearchCriteriaChange = (criteria) => setSearchCriteria(criteria);
  const handleSearchWordChange = (e) => setSearchWord(e.target.value);
  const handleCourseChange = (e) => setSelectedCourse(e.target.value);
  const handleDepartmentChange = (e) => setSelectedDepartment(e.target.value);

  const handleSearch = (type) => {
    console.log(`Searching by ${type}`);
    if (type === 'word') {
      console.log(`Search word: ${searchWord}, Criteria: ${searchCriteria}`);
    } else if (type === 'course') {
      console.log(`Selected course: ${selectedCourse}`);
    } else if (type === 'department') {
      console.log(`Selected department: ${selectedDepartment}`);
    }
  };

  return (
    <div className="e-library-container">
      <div className="container">
        <h1 className="library-title">E - LIBRARY</h1>

        <div className="dotted-border">
          <div className="search-criteria">
            {["Title", "Author", "Course", "Department", "Research Papers"].map((criteria) => (
              <label key={criteria} className="criteria-label">
                <input
                  type="radio"
                  className="criteria-radio"
                  checked={searchCriteria === criteria}
                  onChange={() => handleSearchCriteriaChange(criteria)}
                />
                <span className="criteria-text">{criteria}</span>
              </label>
            ))}
          </div>

          {/* Search Word Section */}
          <div className="search-section">
            <div className="input-group">
              <label className="input-label">Search Word :</label>
              <input
                type="text"
                className="input-field"
                value={searchWord}
                onChange={handleSearchWordChange}
              />
            </div>
            <div className="button-container">
              <button className="search-button" onClick={() => handleSearch('word')}>Search</button>
            </div>
          </div>

          {/* Course Selection Section */}
          <div className="search-section">
            <div className="input-group">
              <label className="input-label">Course :</label>
              <select className="input-field" value={selectedCourse} onChange={handleCourseChange}>
                <option>-Courses-</option>
                {courses.map(course => (
                  <option key={course} value={course}>{course}</option>
                ))}
              </select>
            </div>
            <div className="button-container">
              <button className="search-button" onClick={() => handleSearch('course')}>Search</button>
            </div>
          </div>

          {/* Department Selection Section */}
          <div className="search-section">
            <div className="input-group">
              <label className="input-label">Department :</label>
              <select className="input-field" value={selectedDepartment} onChange={handleDepartmentChange}>
                <option>-Department-</option>
                {departments.map(department => (
                  <option key={department} value={department}>{department}</option>
                ))}
              </select>
            </div>
            <div className="button-container">
              <button className="search-button" onClick={() => handleSearch('department')}>Search</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ELibrary;
