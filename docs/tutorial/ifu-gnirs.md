# GNIRS LR-IFU acquisition

This example is a GNIRS LR-IFU acquisition of a faint target, so sky subtraction
is used. The observation is GN-2024B-Q-204-142. It uses six images:

| Image            | What it is                     | IFU in beam | P (") | Q (") |
|------------------|--------------------------------|-------------|-------|-------|
| N20250115S0234   | Sky for the field image        | no          | 0.0   | 2.0   |
| N20250115S0235   | Field image                    | no          | 0.0   | 0.0   |
| N20250115S0236   | Through-IFU sky (large offset) | yes         | −10.0 | 0.0   |
| N20250115S0237   | Through-IFU sky                | yes         | 10.7  | 3.2   |
| N20250115S0238   | Through-IFU on-target          | yes         | 10.7  | 1.2   |
| N20250115S0239   | Through-IFU on-target          | yes         | 11.2  | 1.2   |

P and Q are the telescope offsets of each image.

The target is faint, so the sequence starts with a sky image at Q = 2.0", then
the field image at zero offset, then the IFU slits image at a large offset. The
observer took the first two images and started the acquisition on the field
image while the third one was still exposing.

## 1. Load the field image

Type `N20250115S0235` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq finds and subtracts the sky image, `N20250115S0234`.

In the **Select Acquisition Type** dialog, select **IFU** and click **Select**.

Pygacq then warns that the CRPA is between 45 and 150 degrees, where the GNIRS
acquisition mirror may drift. The observer decided to go on, so click **Yes**.

:::{figure} images/ifu-gnirs-crpa.png
:width: 60%
:alt: The CRPA warning, asking whether to continue

The CRPA warning.
:::

## 2. Identify the target

This object has a finder chart. To give the acquisition image the same
orientation, North up and East left, click
![](images/icons/orient_ne.svg){w=22px} in the toolbar under the image.

The sky image was taken at too small an offset, so structures from a nearby
object partly cover the target. To see it better, set **Sky** to **User** and
untick the sky image in the **Acquisitions** list, which turns sky subtraction
off.

:::{figure} images/ifu-gnirs-field-image.png
:width: 100%
:alt: The field image without sky subtraction, with the green IFU rectangle

The field image with sky subtraction off. The green rectangle is the IFU field.
:::

## 3. Confirm the target position

From here on, the **Current Acquisition** tab guides you step by step. Read it
at every step.

Mark the target that is to be centered in the IFU field, shown as a green
rectangle: put the cursor on it, press {kbd}`R`, check the fit, then click **Accept**.

## 4. Send the offsets and take the through-IFU images

The offsets are P = 10.823", Q = 1.223", and the advice is to apply them and
take the through-IFU image. To follow it, press {kbd}`Enter`.

At night the observer waited for the third image to finish, applied the offsets,
and took the next two images: the through-IFU sky image and the through-IFU
on-target image.

## 5. Confirm the IFU slice positions

Type `N20250115S0238` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq subtracts the sky image, `N20250115S0237`, and measures the IFU slices on
`N20250115S0236`.

The panel reports **IFU SLICE AUTO-DETECTION COMPLETED**. Check the slice
overlay in the viewer, then click **Accept slice position**.

- **Hide slice overlay** takes the overlay off for a moment.
- **Remeasure slices** measures them again, following the instructions in the
  tab.

:::{figure} images/ifu-gnirs-slices.png
:width: 100%
:alt: The IFU slice overlay on the through-IFU image

The measured IFU slice positions on `N20250115S0236`.
:::

## 6. Confirm the target in the reconstructed image

Pygacq reconstructs the IFU field from the slices, finds the target in it, and
marks it with a red cross. Check the mark, then click **Accept**.

If the target was not found, mark it yourself with {kbd}`R` or {kbd}`X`.

:::{tip}
To acquire the target somewhere other than the center of the IFU, set the
position in **Use custom acquiring position**.
:::

:::{figure} images/ifu-gnirs-reconstructed-with-arrows.png
:width: 100%
:alt: The reconstructed IFU field with the target marked by a red cross

The reconstructed IFU field, with the target marked by a red cross.
:::

## 7. Read the offset advice

The offsets are P = 0.477", Q = −0.031", still above the 0.1" limit, so the
advice is to apply them and take another acquisition image. To follow it, press
{kbd}`Enter`.

The observer took another through-IFU on-target image.

:::{figure} images/ifu-gnirs-offsets.png
:width: 60%
:alt: The offsets page for N20250115S0238, advising to apply the offsets and take another acquisition image

The offsets for `N20250115S0238`: P = 0.477", Q = −0.031".
:::

## 8. Check the centering and start science

Load the last through-IFU image, `N20250115S0239`. In the **Acquisitions** list
you can see that it uses the same sky image as the previous pass,
`N20250115S0237`.

The panel reports *Reusing previous IFU slit measurement from N20250115S0236*,
so the slices are not measured again. The target now looks well centered. Press
{kbd}`Enter`, or click **Accept**, to calculate the offsets.

They are P = −0.091", Q = −0.051", and the grey text says *\|P\| and \|Q\| <
0.1"*. The target is centered in the IFU, so the advice is *Ignore offsets and
start science immediately*. Press {kbd}`Enter` to follow it: the acquisition
ends here.
