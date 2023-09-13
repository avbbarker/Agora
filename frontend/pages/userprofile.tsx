import Image from "next/image";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function UserProfile() {
  return (
    <div
      className={`flex min-h-screen flex-col items-center justify-between p-78 ${inter.className}`}
    >
      <div className="">
        <h1 className="position">User Profile</h1>
      </div>
    </div>
  );
}
