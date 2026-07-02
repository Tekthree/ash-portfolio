type ImageProps = { src: string; alt?: string };

type Props = {
  quote: string;
  avatar: ImageProps;
  name: string;
  position: string;
};

export type Testimonial1Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Testimonial1 = (props: Testimonial1Props) => {
  const { quote, avatar, name, position } = {
    ...Testimonial1Defaults,
    ...props,
  };
  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28 bg-ink text-scheme-background">
      <div className="container w-full max-w-lg">
        <div className="flex flex-col items-center text-center">
          <h5 className="text-h4 font-serif italic font-medium leading-snug">{quote}</h5>
          <div className="mt-6 flex flex-col items-center justify-center md:mt-8">
            <div className="mx-auto mb-3 size-16 min-h-16 min-w-16 overflow-hidden rounded-full md:mb-4">
              <img src={avatar.src} alt={avatar.alt} className="size-full object-cover" />
            </div>
            <div className="flex flex-col items-center justify-center">
              <p className="font-semibold">{name}</p>
              <p className="text-blush">{position}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export const Testimonial1Defaults: Props = {
  quote: "",
  avatar: { src: "", alt: "" },
  name: "",
  position: "",
};
