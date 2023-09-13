// "use client";

// import Image from "next/image";
// import { bodyFont } from "../lib/utils/fonts";

// export default function About() {
//   return (
//     <div>
// <h1
//   className={`flex flex-col items-center justify-between p-78 text-2xl ${bodyFont.className}`}
// >
//   About Us
// </h1>
// <p
//   className={`flex flex-col h-180 items-center justify-between p-78 ${bodyFont.className}`}
// >
//   Agora is a web application for artists, curators, and consumers to buy,
//   share, collect, connect, promote, and commission art of various mediums;
//   from visual art, to music, fashion and more
// </p>
//     </div>
//   );
// }

import Head from "next/head";
import IndexLayout from "../components/layout/IndexLayout";
import { bodyFont } from "../lib/utils/fonts";

function About() {
  return (
    <>
      <Head>
        <title>About</title>
      </Head>
      <h1
        className={`flex flex-col items-center justify-between p-78 text-2xl ${bodyFont.className}`}
      >
        About Us
      </h1>
      <p
        className={`flex flex-col h-180 items-center justify-between p-78 ${bodyFont.className}`}
      >
        Agora is a web application for artists, curators, and consumers to buy,
        share, collect, connect, promote, and commission art of various mediums;
        from visual art, to music, fashion and more
      </p>
    </>
  );
}

About.PageLayout = IndexLayout;

export default About;
