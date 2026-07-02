type ImageProps = { src: string; alt?: string };

type Props = {
  heading: string;
  image: ImageProps;
  children: React.ReactNode;
};

export type Content2Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Content2 = (props: Content2Props) => {
  const { heading, children, image } = {
    ...Content2Defaults,
    ...props,
  };
  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28 bg-scheme-foreground">
      <div className="container">
        <div className="grid grid-cols-1 items-start gap-y-12 md:grid-cols-2 md:gap-x-12 lg:gap-x-20">
          <div>
            <img src={image.src} className="w-full rounded-image object-cover" alt={image.alt} />
          </div>
          <div>
            <h2 className="mb-5 text-h2 font-bold md:mb-6">{heading}</h2>
            <div className="prose-base prose-p:m-0 prose-p:mb-4 prose-p:leading-[1.7] text-ink-soft">
              {children}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export const Content2Defaults: Props = {
  heading: "",
  children: null,
  image: { src: "", alt: "" },
};
