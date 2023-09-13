/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "images.pexels.com",
        port: "",
        pathname: "/photos/**",
      },
    ],
    domains: [
      "external-content.duckduckgo.com",
      "images-na.ssl-images-amazon.com",
      "images.genius.com",
      "s3.amazonaws.com",
      "m.media-amazon.com",
    ],
  },
};
module.exports = nextConfig;
