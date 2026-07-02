import { Button, type ButtonProps } from "@/components/ui/button";

type ImageProps = { src: string; alt?: string };

type Props = {
  heading: React.ReactNode;
  description: string;
  buttons: ButtonProps[];
  firstImage: ImageProps;
  secondImage: ImageProps;
};

export type Header138Props = React.ComponentPropsWithoutRef<"section"> & Partial<Props>;

export const Header138 = (props: Header138Props) => {
  const { heading, description, buttons, firstImage, secondImage } = {
    ...Header138Defaults,
    ...props,
  };
  return (
    <section className="flex min-h-svh flex-col md:h-svh">
      <div className="relative flex flex-1 flex-col">
        <div className="relative flex-1">
          <img
            className="absolute inset-0 aspect-[3/2] size-full object-cover"
            src={firstImage.src}
            alt={firstImage.alt}
          />
        </div>
        <div className="absolute right-[5%] bottom-[-15%] w-[30%] md:w-1/5">
          <img
            className="aspect-square size-full rounded-image object-cover border-8 border-scheme-background"
            src={secondImage.src}
            alt={secondImage.alt}
          />
        </div>
      </div>
      <div className="px-[5%]">
        <div className="container">
          <div className="py-12 md:py-18 lg:py-20">
            <div className="auto-cols-1fr mt-[5%] grid grid-cols-1 items-start gap-5 md:grid-cols-2 md:gap-x-12 md:gap-y-8 lg:gap-x-20 lg:gap-y-16">
              <h1 className="text-h1 font-bold">{heading}</h1>
              <div>
                <p className="text-medium text-ink-soft">{description}</p>
                <div className="mt-6 flex gap-x-4 md:mt-8">
                  {buttons.map((button, index) => (
                    <Button key={index} {...button}>
                      {button.title}
                    </Button>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export const Header138Defaults: Props = {
  heading: "Medium length hero heading goes here",
  description: "",
  buttons: [],
  firstImage: { src: "", alt: "" },
  secondImage: { src: "", alt: "" },
};
