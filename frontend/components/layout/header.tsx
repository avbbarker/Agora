"use client";

import { titleFont } from "../../lib/utils/fonts";

export default function Header() {
  return (
    <div className="h-18 left-0 bg-transparent">
      <h1
        className={`${titleFont.className} text-8xl w-1/4 relative top-14 left-14 animate-fade-in-down`}
      >
        Agora
      </h1>
    </div>
  );
}

// className={UnifrakturCook.className}
