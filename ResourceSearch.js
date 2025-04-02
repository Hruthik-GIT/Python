import { useState, useEffect, useRef } from "react";

export default function ResourceSearch() {
  const [searchKeyword, setSearchKeyword] = useState("");
  const [resourceType, setResourceType] = useState("All");
  const [dropdownOpen, setDropdownOpen] = useState(false);

  // Reference for detecting clicks outside the dropdown
  const dropdownRef = useRef(null);

  const resourceTypes = [
    "E-Book",
    "Tools",
    "Notes",
    "Projects",
    "YouTube Links",
    "Scholarly Papers",
    "Forms",
  ];

  // Close dropdown if clicked outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setDropdownOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  const handleSearch = () => {
    if (!searchKeyword.trim()) {
      alert("Please enter a search keyword.");
      return;
    }
    console.log(`Searching for: ${searchKeyword}, Resource Type: ${resourceType}`);
    // Implement API call here if needed
  };

  return (
    <div className="flex flex-col min-h-screen bg-white p-10">
      <h2 className="text-3xl font-bold text-blue-700 mb-4">RESOURCES</h2>
      <div className="w-full border-t-2 border-dotted border-gray-400 mb-8"></div>

      <div className="flex justify-center">
        <div className="bg-white p-6 rounded-lg shadow-md">
          {/* Search Keyword */}
          <div className="grid grid-cols-2 gap-4 items-center">
            <label className="text-lg font-medium">Search Keyword :</label>
            <input
              type="text"
              value={searchKeyword}
              onChange={(e) => setSearchKeyword(e.target.value)}
              className="border border-gray-400 rounded-md px-3 py-2 w-64"
              placeholder="Enter keyword..."
            />
          </div>

          {/* Dropdown for Resource Type */}
          <div className="grid grid-cols-2 gap-4 items-center mt-4 relative">
            <label className="text-lg font-medium">Resource Type :</label>
            <div className="relative w-64" ref={dropdownRef}>
              <button
                onClick={() => setDropdownOpen(!dropdownOpen)}
                className="border border-gray-400 rounded-md px-3 py-2 w-full text-left flex justify-between items-center"
              >
                {resourceType}
                <span className="ml-2">&#9662;</span>
              </button>

              {dropdownOpen && (
                <div className="absolute bg-white border border-gray-400 rounded-md mt-1 w-full z-10 shadow-lg">
                  {resourceTypes.map((type) => (
                    <div
                      key={type}
                      onClick={() => {
                        setResourceType(type);
                        setDropdownOpen(false);
                      }}
                      className="px-3 py-2 hover:bg-gray-200 cursor-pointer"
                    >
                      {type}
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Search Button */}
          <div className="flex justify-center mt-6">
            <button onClick={handleSearch} className="bg-blue-600 text-white px-6 py-2 rounded-md text-lg">
              Search
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
