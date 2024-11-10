"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card";
import Link from "next/link";

export default function Home() {
  const [currentPage, setCurrentPage] = useState("page1");

  return (
    <div className="min-h-screen flex flex-col items-center">
      {/* NavBar */}
      <nav className="w-full flex justify-between items-center p-6 bg-blue-600 text-white">
        <h1 className="text-2xl font-bold">Speakly</h1>
        <ul className="flex space-x-4">
          <li>
            <HoverCard>
              <HoverCardTrigger asChild>
                <button onClick={() => setCurrentPage("page1")}>Home</button>
              </HoverCardTrigger>
              <HoverCardContent>Go to the landing page</HoverCardContent>
            </HoverCard>
          </li>
          <li>
            <HoverCard>
              <HoverCardTrigger asChild>
                <button onClick={() => setCurrentPage("page2")}>Scenarios</button>
              </HoverCardTrigger>
              <HoverCardContent>Choose a language and scenario</HoverCardContent>
            </HoverCard>
          </li>
          <li>
            <HoverCard>
              <HoverCardTrigger asChild>
                <button onClick={() => setCurrentPage("page3")}>Speak with AI</button>
              </HoverCardTrigger>
              <HoverCardContent>Practice speaking with AI</HoverCardContent>
            </HoverCard>
          </li>
        </ul>
      </nav>

      {/* Page Sections */}
      {currentPage === "page1" && (
        <div className="flex flex-col items-center p-8">
          <h2 className="text-3xl font-bold mb-4">Welcome to Speakly</h2>
          <p className="text-center">
            Learn new languages in realistic scenarios with AI-driven interactions.
          </p>
        </div>
      )}

      {currentPage === "page2" && (
        <div className="flex flex-col items-center p-8">
          <h2 className="text-3xl font-bold mb-4">Choose Your Scenario</h2>
          <p>Select a language and scenario to get started.</p>
          {/* Add your language and scenario options here */}
        </div>
      )}

      {currentPage === "page3" && (
        <div className="flex flex-col items-center p-8">
          <h2 className="text-3xl font-bold mb-4">Speak with AI</h2>
          <p>Click the button below to start speaking with our AI.</p>
          <Button>Speak Now</Button>
        </div>
      )}
    </div>
  );
}
