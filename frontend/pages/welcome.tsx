import Head from "next/head";
import IndexLayout from "../components/layout/IndexLayout";
import { bodyFont } from "../lib/utils/fonts";

function Welcome() {
  return (
    <>
      <Head>
        <title>Welcome</title>
      </Head>
      <h1
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
      </div>
    </>
  );
}

Welcome.PageLayout = IndexLayout;

export default Welcome;
