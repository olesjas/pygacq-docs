# GMOS-N MOS acquisition (starting with mask out)

This example starts with the mask out of the beam. The observation is GN-2026A-LP-207-55, with the mask `GN2024ALP207-03`.
It uses three images:

| Image            | What it is      | Mask in beam | P (") | Q (")  |
|------------------|-----------------|--------------|-------|--------|
| N20260309S0096   | Field image     | no           | 0.0   | 0.0    |
| N20260309S0097   | Mask-in image   | yes          | 0.0   | −0.4   |
| N20260309S0098   | Mask-in image   | yes          | −0.1  | −0.1   |

P and Q are the telescope offsets of each image.

The acquisition stars are aligned with the square acquisition holes (boxes) of the mask.
Pygacq reads the box positions from the mask definition file (MDF), found by the
mask name.

The observer took the first image of the field without the MOS mask in, then
started the acquisition on it.

## 1. Load the field image

:::{admonition} Demonstration only
:class: attention

First click the acquisition options button, to the right of the *Enter image
number* box, and tick **Manual acquisition type**. It makes the flow match the
one at night. Skip it when observing.
:::

Type `N20260309S0096` in the *Enter image number* box and press {kbd}`Enter`.

In the **Select Acquisition Type** dialog, select **MOS**. Pygacq fills in the
**Mask number** box with the program part from the current observation,
`GN2026ALP207`. This mask was made in an earlier semester, so change it to
`GN2024ALP207`, type `3` after the dash, and click **Select**.

:::{figure} images/mos-type-dialog.png
:width: 50%
:alt: The Select Acquisition Type dialog with MOS selected and GN2024ALP207-2 as the mask number

**MOS** selected, with the program part changed to `GN2024ALP207`.
:::

:::{tip}
The mask number can be found in the OT, under **Observation → Instrument → Custom MDF**.
:::

The acquisition starts with finding the acquisition stars near the box positions from the MDF.

## 2. Confirm the acquisition stars

From here on, the **Current Acquisition** tab guides you step by step. Read it
at every step.

Pygacq looks for stars near each box position that share a common offset, and
shows them in a collage: one small image per box, with a red cross on each star
it found. The panel says how many stars it identified.

Check that each numbered box has a star identified. Here all 4 stars were found
and look correct, so click **Accept star positions**.

:::{tip}
Click **Display individual boxes** to see each box position in the full image,
e.g. when a collage cell has no star.
:::

:::{figure} images/mos-star-collage-with-arrows.png
:width: 100%
:alt: The Confirm acq. stars step on the field image: a red cross on each of the 4 stars, next to the green box positions from the MDF

All 4 stars found, each marked with a red cross. The green squares are the box
positions from the MDF.
:::

## 3. Send the offsets and take the mask-in image

Pygacq shows the offsets, including a rotation, **Rot**. With no mask in the
beam, the advice is to apply them and take an image through the MOS mask. To
follow it, press {kbd}`Enter`.

That ends this pass of the acquisition. At night, you would now take the next
image of the sequence, with the mask in.

## 4. Confirm the acquisition boxes

Type `N20260309S0097` in the *Enter image number* box and press {kbd}`Enter`.

The mask is in the beam now, so the first step is **Confirm acq. boxes**. Pygacq
traces the acquisition boxes and shows them in a collage, with a green square on
each box it found.

Check that each green square matches its box. If the overlay is in
  the way, click the green X in the box first.

Then click **Accept box positions**.

:::{figure} images/mos-box-collage.png
:width: 100%
:alt: The Confirm acq. boxes step: a collage of the 4 acquisition boxes with green squares

All 4 acquisition boxes identified, each with a green square.
:::

## 5. Confirm the acquisition stars in the boxes

The next step is to confirm the stars that Pygacq found in the boxes. The collage
looks almost the same as in the previous step, except that the red crosses now
appear. Check that every box has a red cross, then click **Accept star
positions**.

:::{figure} images/mos-stars-in-boxes.png
:width: 100%
:alt: The Confirm acq. stars step: the same collage with a red cross on the star in each box

The same collage, now with a red cross on the star in each box.
:::

## 6. Read the offset advice

Pygacq fits the mask to the star positions. The grey text under the offsets
says why it gives its advice, here *\|P\|+\|R\| = 5% of slit width,
\|Q\|+\|R\| > 0.2"*. There, \|R\| is the shift that the rotation causes at the
edge of the field.

Here the stars are still off the box centers, so the advice is to apply the
offsets and take another acquisition image. To follow it, press {kbd}`Enter`.

:::{figure} images/mos-offsets.png
:width: 60%
:alt: The offsets page for N20260309S0097, advising to apply the offsets and take another acquisition image

The offsets for `N20260309S0097`.
:::

## 7. Check the alignment and start science

Load the next mask-in image, `N20260309S0098`, and repeat
[steps 4](#4-confirm-the-acquisition-boxes) to
[6](#6-read-the-offset-advice).

This time the stars are well centered in the boxes, so the advice is to ignore
the offsets and start science. To follow it, press {kbd}`Enter`.
