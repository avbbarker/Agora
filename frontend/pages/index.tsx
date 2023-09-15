// "use client";

// import Image from "next/image";
// import { Inter } from "next/font/google";
// import React from "react";
// import { useRouter } from "next/router";
// import Error from "./error";
// import Welcome from "./welcome";
// import Gallery from "./gallery";
// import About from "./about";
// import UserProfile from "./userProfile";

// const inter = Inter({ subsets: ["latin"] });

// const Index = () => {
//   const router = useRouter();

//   return (
//     <main
//     // className={`flex min-h-screen flex-col items-center justify-between p-78 ${inter.className}`}
//     >
//       <React.StrictMode>
//         {/* {router.pathname === "/" && <Welcome />}
//         {router.pathname === "/gallery" && <Gallery />}
//         {router.pathname === "/about" && <About />}
//         {router.pathname === "/error" && <Error />}
//         {router.pathname === "/userprofile" && <UserProfile />} */}
//       </React.StrictMode>
//     </main>
//   );
// };

// export default Index;

import Head from "next/head";
import IndexLayout from "../components/layout/IndexLayout";
import { Auth } from "../components/auth/components/auth";
import { bodyFont } from "../lib/utils/fonts";

function Home() {
  return (
    <>
      <Head>
        <title>Login</title>
      </Head>
      {/* <h1
        className={`absolute top-60 text-9xl flex h-60 w-full flex-col items-center justify-center p-10 animate-fade-in-down ${bodyFont.className}`}
      >
        Welcome to Agora
      </h1>
      <p
        className={`absolute top-96 text-8xl flex h-60 w-full flex-col items-center justify-center p-78 animate-fade-in-down ${bodyFont.className}`}
      >
        Where creatives connect.
      </p>
      <div className="bg-white min-h-screen flex items-center justify-center px-16">
        <div className="relative w-full max-w-lg">
          <div className="absolute top-0 right-0 w-180 h-180 bg-amber-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-fade-background"></div>
          <div className="absolute top-0 -right-96 w-180 h-180 bg-red-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-fade-background animation-delay-5000"></div>
          <div className="absolute top-0 -left-96 w-180 h-180 bg-cyan-200 rounded-full mix-blend-multiply filter blur-xl opacity-70 animate-fade-background animation-delay-10000"></div>
          <div className="m-8 relative space-y-4"></div>
        </div>
      </div> */}
      <Auth />
    </>
  );
}

Home.PageLayout = IndexLayout;

export default Home;
