# F2 MOS acquisition (with sky subtraction)

This example starts with the mask out of the beam. The observation is
GS-2025A-Q-140-705, with the mask `GS2025AQ140-01`. It uses six images:

| Image            | What it is                 | Mask in beam | P (") | Q (")  |
|------------------|----------------------------|--------------|-------|--------|
| S20250625S0111   | Sky for the field image    | no           | 0.0   | 10.0   |
| S20250625S0112   | Field image                | no           | 0.0   | 0.0    |
| S20250625S0113   | Sky for the mask-in images | yes          | 3.7   | 11.4   |
| S20250625S0114   | Mask-in image              | yes          | 3.7   | 1.4    |
| S20250625S0115   | Mask-in image              | yes          | 3.0   | 1.5    |
| S20250625S0116   | Mask-in image              | yes          | 2.9   | 1.4    |

P and Q are the telescope offsets of each image. The sky images are taken 10"
away in Q from the on-target images.

The acquisition stars are aligned with the square acquisition holes (boxes) of the mask.
Pygacq reads the box positions from the mask definition file (MDF), found by the
mask name.

The observer took the first two images without the MOS mask in, then
started the acquisition on the second.

## 1. Load the field image

:::{admonition} Demonstration only
:class: attention

First click the acquisition options button, to the right of the *Enter image
number* box, and tick **Manual acquisition type**. It makes the flow match the
one at night. Skip it when observing.
:::

Type `S20250625S0112` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq finds and subtracts the sky image, `S20250625S0111`.

In the **Select Acquisition Type** dialog, select **MOS**. Pygacq fills in the
**Mask number** box with the program part from the current observation,
`GS2025AQ140`. Type `1` after the dash and click **Select**.

:::{note}
Some masks are made for an earlier program. Then correct the program part as
well, as in
[the GMOS-N example](mos-gmos-n.md#1-load-the-field-image).
:::

:::{tip}
The mask number can be found in the OT, under **Observation → Instrument → Custom MDF**.
:::

The acquisition starts with finding the acquisition stars near the box positions from the MDF.

:::{figure} images/mos-f2-type-dialog.png
:width: 50%
:alt: The Select Acquisition Type dialog with MOS selected and GS2025AQ140-1 as the mask number

**MOS** selected, with `GS2025AQ140` filled in and `1` typed after the dash.
:::

## 2. Confirm the acquisition stars

From here on, the **Current Acquisition** tab guides you step by step. Read it
at every step.

Pygacq looks for stars near each box position that share a common offset, and
shows them in a collage: one small image per box, with a red cross on each star
it found. The panel says how many stars it identified.

Check that each numbered box has a star identified. Here all 3 stars were found
and look correct, so click **Accept star positions**.

:::{tip}
Click **Display individual boxes** to see each box position in the full image,
e.g. when a collage cell has no star.
:::

:::{figure} images/mos-f2-star-collage.png
:width: 100%
:alt: The Confirm acq. stars step on the field image: a red cross on each of the 3 stars, next to the green box positions from the MDF

All 3 stars found, each marked with a red cross. The green squares are the box
positions from the MDF.
:::

## 3. Send the offsets and take the mask-in image

Pygacq shows the offsets, including a rotation, **Rot**: P = 3.586", Q = 1.384",
Rot = −0.241°. The advice is to apply them and take an
image through the MOS mask. To follow it, press {kbd}`Enter`.

That ends this pass of the acquisition. At night, you would now take the next
images of the sequence, the sky image and the mask-in image.

## 4. Confirm the acquisition boxes

Type `S20250625S0114` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq subtracts the sky image taken at the new position, `S20250625S0113`.

The **Acquisitions** list has a tick for `S20250625S0113` in both **Sky** and
**Slit**: the boxes are measured on the sky image, where the stars are out of
them.

The mask is in the beam now, so the first step is **Confirm acq. boxes**. Pygacq
traces the acquisition boxes on the sky offset image, and shows them in a
collage, with a green square on each box it found.

Check that each green square matches its box. If the overlay is in
  the way, click the green X in the box first.

Then click **Accept box positions**.

:::{figure} images/mos-f2-box-collage.png
:width: 100%
:alt: The Confirm acq. boxes step: a collage of the 3 acquisition boxes with green squares

All 3 acquisition boxes identified on the sky image, each with a green square.
:::

## 5. Confirm the acquisition stars in the boxes

The next step is to confirm the stars that Pygacq found in the boxes. This
collage is cut from the sky-subtracted acquisition image, so each box now holds
its star, with a red cross on it. Check that every box has one, then click
**Accept star positions**.

## 6. Read the offset advice

Pygacq fits the mask to the star positions. The grey text under the offsets
says why it gives its advice, here *\|P\|+\|R\| > 0.2", \|Q\|+\|R\| > 0.2"*.
There, \|R\| is the shift that the rotation causes at the edge of the field.

Here the stars are still off the box centers, so the advice is to apply the
offsets and take another acquisition image. To follow it, press {kbd}`Enter`.

:::{figure} images/mos-f2-offsets.png
:width: 60%
:alt: The offsets page for S20250625S0114, advising to apply the offsets and take another acquisition image

The offsets for `S20250625S0114`: P = −0.591", Q = 0.162", Rot = −0.038°.
:::

## 7. Check the alignment

Type `S20250625S0115` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq subtracts the same sky image as in the previous pass, `S20250625S0113`.

The box measurements from `S20250625S0114` are reused, so the **Confirm acq.
boxes** step is skipped. The star page says which image they come from:
*Reusing acq. box measurements from S20250625S0114*.

Confirm the stars as in
[step 5](#5-confirm-the-acquisition-stars-in-the-boxes), then read the offset
advice as in [step 6](#6-read-the-offset-advice).

:::{note}
To check the reused boxes, or to measure them again on this image, click the
**Confirm acq. boxes** step button.
:::

The offsets are much smaller, P = −0.037", Q = 0.042", Rot = −0.018°, but still
over the limit, so the advice is again to apply them and take another
acquisition image.

## 8. Check the alignment and start science

Load `S20250625S0116`. It uses the same sky image again, and the box
measurements are reused again, so repeat
[steps 5](#5-confirm-the-acquisition-stars-in-the-boxes) and
[6](#6-read-the-offset-advice).

The stars are centered in the boxes now: the offsets are P = −0.001",
Q = 0.022", Rot = 0.017°, all within the limits, so the advice is to ignore them
and start science. To follow it, press {kbd}`Enter`.
