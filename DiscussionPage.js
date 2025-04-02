import { useState } from "react";

// Component for the discussion page functionality
export default function DiscussionPage() {
  const [topicName, setTopicName] = useState("");
  const [discussions, setDiscussions] = useState([]);

  // Function to handle adding a new topic
  const handleAddTopic = () => {
    if (!topicName.trim()) return; // Prevent adding empty topics
    setDiscussions([...discussions, topicName]); // Add topic to state
    setTopicName(""); // Clear input field
  };

  return (
    <div className="flex flex-col min-h-screen bg-white p-10">
      {/* Page title */}
      <h2 className="text-3xl font-bold text-blue-700 mb-4">Discussions</h2>

      {/* Dotted divider */}
      <div className="w-full border-t-2 border-dotted border-gray-400 mb-8"></div>

      {/* Discussion Form */}
      <div className="flex justify-center">
        <div className="bg-white p-6 rounded-lg shadow-md">
          
          {/* Done Button */}
          <div className="flex justify-start mb-4">
            <button className="bg-green-600 text-white px-6 py-2 rounded-md text-lg flex items-center">
              ✓ Done
            </button>
          </div>

          {/* Input field for topic name */}
          <div className="grid grid-cols-1 gap-4 items-center">
            <input
              type="text"
              value={topicName}
              onChange={(e) => setTopicName(e.target.value)}
              className="border border-gray-400 rounded-md px-3 py-2 w-96 text-center"
              placeholder="Enter a discussion topic"
            />
          </div>

          {/* Buttons */}
          <div className="flex justify-between mt-6">
            <button onClick={handleAddTopic} className="bg-blue-900 text-white px-6 py-2 rounded-md text-lg">
              Add discussion topic
            </button>
            <button className="bg-blue-900 text-white px-6 py-2 rounded-md text-lg">
              Participants
            </button>
          </div>
        </div>
      </div>

      {/* Discussion List */}
      <div className="flex flex-col items-center mt-10 w-full">
        <p className="text-lg text-gray-700 mb-4">Discussion Topics</p>
        
        {discussions.length === 0 ? (
          <p className="text-gray-500">No topics yet. Add one above!</p>
        ) : (
          <ul className="w-2/3">
            {discussions.map((topic, index) => (
              <li key={index} className="bg-gray-200 p-3 mb-2 rounded-md shadow-md text-center">
                {topic}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}
