import "../styles/globals.css";
import Header from "../components/layout/header";
import Nav from "../components/layout/nav";
import Footer from "../components/layout/footer";
import "animate.css/animate.min.css";
import type { AppProps } from "next/app";

type CustomAppProps<P = {}> = AppProps<P> & {
  Component: React.ComponentType<P> & {
    PageLayout?: React.ComponentType;
  };
};

function MyApp({ Component, pageProps }: CustomAppProps) {
  return (
    <div>
      <Nav />
      <Header />
      {Component.PageLayout ? (
        <Component.PageLayout>
          <Component {...pageProps} />
        </Component.PageLayout>
      ) : (
        <Component {...pageProps} />
      )}
      <Footer />
    </div>
  );
}

export default MyApp;
