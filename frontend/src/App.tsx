import { useState } from 'react'

function App() {
  const [activeTab, setActiveTab] = useState('overview');

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col">
      {/* Navigation Bar */}
      <nav className="bg-gray-800 p-4 shadow-md flex justify-between items-center">
        <div className="flex items-center space-x-4">
          <span className="text-xl font-bold tracking-wider text-blue-400">Aegentis</span>
          <div className="hidden md:flex space-x-2">
            <button
              onClick={() => setActiveTab('overview')}
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${activeTab === 'overview' ? 'bg-gray-700 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white'}`}
            >
              Overview
            </button>
            <button
              onClick={() => setActiveTab('incidents')}
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${activeTab === 'incidents' ? 'bg-gray-700 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white'}`}
            >
              Incidents
            </button>
            <button
              onClick={() => setActiveTab('environments')}
              className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${activeTab === 'environments' ? 'bg-gray-700 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white'}`}
            >
              Environments
            </button>
          </div>
        </div>
      </nav>

      {/* Main Content Area */}
      <main className="flex-grow p-6">
        <div className="max-w-7xl mx-auto">
          {activeTab === 'overview' && (
            <div>
              <h1 className="text-2xl font-semibold mb-6">Overview Dashboard</h1>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-gray-800 p-4 rounded-lg shadow border border-gray-700">
                  <h2 className="text-gray-400 text-sm">Active Incidents</h2>
                  <p className="text-3xl font-bold mt-2">0</p>
                </div>
                <div className="bg-gray-800 p-4 rounded-lg shadow border border-gray-700">
                  <h2 className="text-gray-400 text-sm">Awaiting Approval</h2>
                  <p className="text-3xl font-bold mt-2 text-yellow-500">0</p>
                </div>
                <div className="bg-gray-800 p-4 rounded-lg shadow border border-gray-700">
                  <h2 className="text-gray-400 text-sm">Verified Recoveries</h2>
                  <p className="text-3xl font-bold mt-2 text-green-500">0</p>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'incidents' && (
            <div>
              <h1 className="text-2xl font-semibold mb-6">Incidents</h1>
              <div className="bg-gray-800 rounded-lg shadow border border-gray-700 overflow-hidden">
                <div className="p-4 text-center text-gray-400 py-12">
                  No incidents currently found.
                </div>
              </div>
            </div>
          )}

          {activeTab === 'environments' && (
            <div>
              <h1 className="text-2xl font-semibold mb-6">Environments</h1>
              <div className="bg-gray-800 rounded-lg shadow border border-gray-700 overflow-hidden">
                <div className="p-4 text-center text-gray-400 py-12">
                  No environments configured yet.
                </div>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  )
}

export default App
