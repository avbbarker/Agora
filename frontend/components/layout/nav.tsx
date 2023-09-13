"use client";

import Link from "next/link";

import { bodyFont } from "../../lib/utils/fonts";

export default function Nav() {
  return (
    <>
      <div className="fixed top-0 flex w-full justify-center z-30 transition-all bg-white bg-opacity-70 backdrop-blur-md">
        <div className="mx-5 flex h-16 w-full max-w-screen-xl items-center justify-around px-32 animate-fade-in-down">
          <Link
            href="/welcome"
            className="flex items-center font-display text-2xl"
          >
            <img
              src="https://cdn.iconscout.com/icon/premium/png-256-thumb/parthenon-5454540-4539987.png?f=webp"
              alt="Agora"
              width="30"
              height="30"
              className="mr-2 rounded-sm"
            ></img>
            <h1 className={`${bodyFont.className}`}>Home</h1>
          </Link>
          <Link
            href="/gallery"
            className="flex items-center font-display text-2xl"
          >
            <img
              src="https://cdn-icons-png.flaticon.com/512/2560/2560742.png"
              alt="Gallery"
              width="30"
              height="30"
              className="mr-2 rounded-sm"
            ></img>
            <h1 className={`${bodyFont.className}`}>Gallery</h1>
          </Link>
          <Link
            href="/music"
            className="flex items-center font-display text-2xl"
          >
            <img
              src="https://cdn.iconscout.com/icon/premium/png-256-thumb/vinyl-record-player-2079250-1752059.png?f=webp"
              alt="Music"
              width="30"
              height="30"
              className="mr-2 rounded-sm"
            ></img>
            <h1 className={`${bodyFont.className}`}>Music</h1>
          </Link>
          <Link
            href="/userprofile"
            className="flex items-center font-display text-2xl"
          >
            <img
              // src="https://cdn.iconscout.com/icon/free/png-256/free-account-avatar-profile-human-man-user-30448.png?f=webp"
              src="https://cdn0.iconfinder.com/data/icons/web-and-marketing-glyph/64/web-and-marketing-glyph-02-512.png"
              alt="Profile"
              width="30"
              height="30"
              className="mr-2 rounded-sm"
            ></img>
            <h1 className={`${bodyFont.className}`}>Profile</h1>
          </Link>
          <Link
            href="/about"
            className="flex items-center font-display text-2xl"
          >
            <img
              src="https://cdn-icons-png.flaticon.com/512/8293/8293850.png"
              alt="About Us"
              width="30"
              height="30"
              className="mr-2 rounded-sm"
            ></img>
            <h1 className={`${bodyFont.className}`}>About Us</h1>
          </Link>
        </div>
      </div>
    </>
  );
}
