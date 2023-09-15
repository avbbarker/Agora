// "use client";
// import { bodyFont } from "../lib/utils/fonts";
// import UploadForm from "../components/ui/uploadForm";

// export default function Gallery() {
//   return (
//     <div>
//       <div className="gallery-page">
// <h1
//   className={`flex h-24 flex-col items-center justify-between p-78 text-4xl ${bodyFont.className}`}
// >
//   Gallery
// </h1>
//         <div></div>
//       </div>
//     </div>
//   );
// }

// import Head from "next/head";
// import { bodyFont } from "../lib/utils/fonts";
// import { GalleryLayout } from "../components/layout/GalleryLayout";

// function Gallery() {
//   // const { team, status } = useFetchTeam();

//   return (
//     <>
//       <Head>
//         <title>Gallery</title>
//       </Head>

// <h1
//   className={`flex h-24 flex-col items-center justify-between p-78 text-4xl ${bodyFont.className}`}
// >
//   Gallery
// </h1>
//     </>
//   );
// }

// Gallery.PageLayout = GalleryLayout;

// export default Gallery;

// import Head from "next/head";
// import { bodyFont } from "../lib/utils/fonts";
// import GalleryLayout from "../components/layout/GalleryLayout";

// function Gallery() {
//   return (
//     <div className="h-full w-full">
//       <Head>
//         <title>Team</title>
//       </Head>
//       <h1
//         className={`flex h-24 flex-col items-center justify-between p-78 text-4xl ${bodyFont.className}`}
//       >
//         Gallery
//       </h1>
//       <div className="border-8 w-2/5 h-full">SideMenu</div>
//       <div className="border-8 w-3/5 h-96 absolute inset-y-0 right-0">
//         GalView
//       </div>
//     </div>
//   );
// }

// Gallery.PageLayout = GalleryLayout;

// export default Gallery;

import { Metadata } from "next";
import Image from "next/image";
// import { PlusCircledIcon } from "@radix-ui/react-icons";

import Head from "next/head";
import { bodyFont } from "../lib/utils/fonts";

import { Button } from "../components/ui/button";
import { ScrollArea, ScrollBar } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

import { AlbumArtwork } from "../components/gallery/components/gallery";
import { Menu } from "../components/gallery/components/menu";
import { PodcastEmptyPlaceholder } from "../components/gallery/components/curation";
import { Sidebar } from "../components/gallery/components/sidebar";
import {
  listenNowAlbums,
  madeForYouAlbums,
} from "../components/gallery/data/art";
import { curations } from "../components/gallery/data/curation";

export const metadata: Metadata = {
  title: "Music App",
  description: "Example music app using the components.",
};

export default function MusicPage() {
  return (
    <>
      <Head>
        <title>Gallery</title>
      </Head>

      <h1
        className={`flex h-24 flex-col items-center justify-between p-78 text-9xl ${bodyFont.className}`}
      >
        Gallery
      </h1>
      <div className="md:hidden">
        <Image
          src="/examples/music-light.png"
          width={1280}
          height={1114}
          alt="Music"
          className="block dark:hidden"
        />
        <Image
          src="/examples/music-dark.png"
          width={1280}
          height={1114}
          alt="Music"
          className="hidden dark:block"
        />
      </div>
      <div className="hidden md:block">
        <Menu />
        <div className="border-t">
          <div className="bg-background">
            <div className="grid lg:grid-cols-5">
              <Sidebar curations={curations} className="hidden lg:block" />
              <div className="col-span-3 lg:col-span-4 lg:border-l">
                <div className="h-full px-4 py-6 lg:px-8">
                  <Tabs defaultValue="music" className="h-full space-y-6">
                    <div className="space-between flex items-center">
                      <TabsList>
                        <TabsTrigger value="music" className="relative">
                          Gallery
                        </TabsTrigger>
                        <TabsTrigger value="podcasts">Oeuvre</TabsTrigger>
                      </TabsList>
                      <div className="ml-auto mr-4">
                        {/* <Button>
                          <PlusCircledIcon className="mr-2 h-4 w-4" />
                          Add Piece
                        </Button> */}
                      </div>
                    </div>
                    <TabsContent
                      value="music"
                      className="border-none p-0 outline-none"
                    >
                      <div className="flex items-center justify-between">
                        <div className="space-y-1">
                          <h2 className="text-2xl font-semibold tracking-tight">
                            Discover
                          </h2>
                          <p className="text-sm text-muted-foreground">
                            Browse Artists' Pieces.
                          </p>
                        </div>
                      </div>
                      <Separator className="my-4" />
                      <div className="relative h-256">
                        <ScrollArea>
                          <div className="flex grid grid-cols-5 p-4 w-full h-256 overflow-y-auto">
                            {listenNowAlbums.map((album) => (
                              <AlbumArtwork
                                key={album.name}
                                album={album}
                                className="w-[330px] pb-10"
                                aspectRatio="portrait"
                                width={330}
                                height={1000}
                              />
                            ))}
                          </div>
                          <ScrollBar orientation="vertical" />
                        </ScrollArea>
                      </div>
                      <div className="mt-6 space-y-1">
                        <h2 className="text-2xl font-semibold tracking-tight">
                          Curations
                        </h2>
                        <p className="text-sm text-muted-foreground">
                          Your personal Curations.
                        </p>
                      </div>
                      <Separator className="my-4" />
                      <div className="relative h-98">
                        <ScrollArea>
                          <div className="flex space-x-8 p-4 w-full h-98 overflow-y-auto">
                            {madeForYouAlbums.map((album) => (
                              <AlbumArtwork
                                key={album.name}
                                album={album}
                                className="w-[250px] pb-10"
                                aspectRatio="portrait"
                                width={330}
                                height={330}
                              />
                            ))}
                          </div>
                          <ScrollBar orientation="horizontal" />
                        </ScrollArea>
                      </div>
                    </TabsContent>
                    <TabsContent
                      value="podcasts"
                      className="h-full flex-col border-none p-0 data-[state=active]:flex"
                    >
                      <div className="flex items-center justify-between">
                        <div className="space-y-1">
                          <h2 className="text-2xl font-semibold tracking-tight">
                            Oeuvre
                          </h2>
                          <p className="text-sm text-muted-foreground">
                            Your body of work.
                          </p>
                        </div>
                      </div>
                      <Separator className="my-4" />
                      <PodcastEmptyPlaceholder />
                    </TabsContent>
                  </Tabs>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
