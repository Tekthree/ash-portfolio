import { Button, type ButtonProps } from "@/components/ui/button";

type ImageProps = { src: string; alt?: string };

type Props = {
  heading: string;
  description: string;
  buttons: ButtonProps[];
  image: ImageProps;
};

export type Cta1Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Cta1 = (props: Cta1Props) => {
  const { heading, description, buttons, image } = {
    ...Cta1Defaults,
    ...props,
  };
  return (
    <section className="px-[5%] py-16 md:py-24 lg:py-28 bg-terracotta text-white">
      <div className="container">
        <div className="grid grid-cols-1 gap-x-20 gap-y-12 md:gap-y-16 lg:grid-cols-2 lg:items-center">
          <div>
            <h2 className="mb-5 text-h2 font-bold md:mb-6">{heading}</h2>
            <p className="text-medium opacity-90">{description}</p>
            <div className="mt-6 flex flex-wrap gap-4 md:mt-8">
              {buttons.map((button, index) => (
                <Button key={index} variant="alternate" {...button}>
                  {button.title}
                </Button>
              ))}
            </div>
          </div>
          <div>
            <img src={image.src} className="w-full rounded-image object-cover" alt={image.alt} />
          </div>
        </div>
      </div>
    </section>
  );
};

export const Cta1Defaults: Props = {
  heading: "",
  description: "",
  buttons: [],
  image: { src: "", alt: "" },
};
