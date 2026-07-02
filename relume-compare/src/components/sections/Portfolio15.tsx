import { Badge } from "@/components/ui/badge";
import { Button, type ButtonProps } from "@/components/ui/button";

type ImageProps = { src: string; alt?: string };
type Tag = { label: string; url: string };

type ProjectProps = {
  title: string;
  description: string;
  image: ImageProps;
  url: string;
  button: ButtonProps;
  tags: Tag[];
};

type Props = {
  tagline: string;
  heading: string;
  description: string;
  projects: ProjectProps[];
  button: ButtonProps;
};

export type Portfolio15Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Portfolio15 = (props: Portfolio15Props) => {
  const { tagline, heading, description, projects, button } = {
    ...Portfolio15Defaults,
    ...props,
  };
  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28">
      <div className="container">
        <header className="mb-12 max-w-lg md:mb-18 lg:mb-20">
          <p className="mb-3 font-semibold md:mb-4 text-terracotta uppercase tracking-[.2em] text-tiny">{tagline}</p>
          <h2 className="mb-5 text-h2 font-bold md:mb-6">{heading}</h2>
          <p className="text-medium text-ink-soft">{description}</p>
        </header>
        <div>
          {projects.map((project, index) => (
            <Project key={index} {...project} />
          ))}
        </div>
        <footer className="mt-12 flex justify-center md:mt-18 lg:mt-20">
          <Button {...button}>{button.title}</Button>
        </footer>
      </div>
    </section>
  );
};

const Project: React.FC<ProjectProps> = ({ title, description, image, url, button, tags }) => (
  <article className="grid grid-cols-1 items-center gap-x-12 gap-y-6 border-t border-scheme-border py-8 md:grid-cols-2 md:gap-y-0 lg:gap-x-[4.9rem] lg:py-12">
    <div>
      <h3 className="mb-2 text-h4 font-bold">
        <a href={url}>{title}</a>
      </h3>
      <p className="text-ink-soft">{description}</p>
      <div className="mt-3 flex flex-wrap gap-2 md:mt-4">
        {tags.map((tag, index) => (
          <Badge key={index}>
            <a href={tag.url}>{tag.label}</a>
          </Badge>
        ))}
      </div>
      <Button {...button} asChild className="mt-6 md:mt-8">
        <a href={url}>{button.title}</a>
      </Button>
    </div>
    <div>
      <a href={url} className="flex aspect-[4/3] w-full">
        <img src={image.src} className="w-full rounded-image object-cover" alt={image.alt} />
      </a>
    </div>
  </article>
);

export const Portfolio15Defaults: Props = {
  tagline: "Portfolio",
  heading: "",
  description: "",
  projects: [],
  button: { title: "View all", variant: "secondary" },
};
