# 10x Interpolation Miniproject

## Background

In a previous [10x discussion](http://innolitics.com/10x/discussions/) we read through the [topical review on medical image registration by Derek L. G. Hill et. al.](http://iopscience.iop.org/article/10.1088/0031-9155/46/3/201/meta).  Section 9, which discussed the proper use of interpolation during registration, was quite interesting.  Section 9 is reproduced below:

> Image registration using voxel similarity measures involves determining the transformation T that relates the domain of image A to image B. This transformation can then be used to transform one image into the coordinates of the second within the region of overlap of the two domains. As discussed in section 2 above, this process involves interpolation, and needs to take account of the difference in sample spacing in images A and B.
> 
> *Section 9.1 A consideration of sampling and interpolation theory*
>
> Shannon (1949) showed that a bandlimited signal sampled with an infinite periodic sampling function can be perfectly interpolated using the sinc function interpolant previously proposed by the mathematician Whittaker (1935). Many medical images are, however, not bandlimited. For example, multislice datasets are not bandlimited in the through-slice direction, as the field of view is truncated with a top-hat function. Even in MR image volumes reconstructed using a 3D Fourier transform, the condition is not usually satisfied because the image data provided by the scanner are often truncated to remove slices at the periphery at the field of view. Also the data provided are usually the modulus of the signal, and taking the modulus is a nonlinear operation that can increase the spatial frequency content.
> 
> Even if the images being transformed were strictly bandlimited, it would not be possible to carry out perfect interpolation using a sinc function because a sinc function is infinite in extent.
> 
> For many purposes, this problem is entirely ignored during medical image analysis. The most widely used image interpolation function is probably trilinear interpolation, in which a voxel value in the transformed coordinates is estimated by taking a weighted average of the nearest eight neighbours in the original dataset. The weightings, which add up to one, are inversely proportional to the distance of each neighbour to the new sample point. For the accurate comparison of registered images, for example by subtracting one image from another, the errors introduced by trilinear interpolation become important. It can be shown that trilinear interpolation applies a low-pass filter to the image and introduces aliasing (Parker et al 1983). For transformations that contain rotations, the amount of low-pass filtering varies with position in the image. If subtracting one image from another to detect small change, for example in serial MR imaging, the low-pass filtering in this process can lead to substantial artefacts. Subtracting a low-pass filtered version of an image from the original is a well known edge enhancement method, so even in the case of identical images differing only by a rigid body transformation, using linear interpolation followed by subtraction does not result in the expected null result but instead results in an edge enhanced version of the original.
> 
> Hajnal et al (1995a) recently brought this issue to the attention of MR image analysts and proposed that the solution is to interpolate using a sinc function truncated with a suitable window function such as a Hamming window. Care must be taken when truncating the interpolation kernel to ensure that the integral of the weights of the truncated kernel is unity, or an artefactual intensity modulation can result (Thacker et al 1999).
> 
> Various modifications to sinc interpolation have recently been proposed. These fall into three categories. Firstly, the use of sinc functions with various radii truncated with various window functions (Lehmann et al 1999). Secondly, approximations to windowed sinc functions such as cubic or B-spline interpolants (Lehmann et al 1999, Unser 1999). Thirdly, the shear transform, which involves transforming the image using a combination of shears (Eddy et al 1996, Cox and Jesmanowicz 1999). This third approach is fast, though it does result in artefacts in the corners of the image which must be treated with caution.
> 
> An assumption implicit in the discussion above is that the original data being interpolated are uniformly sampled. This is not always the case in medical images. MR physics researchers are used to the problem of non-uniform sampling in the acquisition, or k-space domain (Robson et al 1997, Atkinson et al 2000), but this problem is less often considered in the spatial domain. The most common circumstances when non-uniform sampling arises are in free- hand 3D ultrasound acquisition and certain types of CT acquisition where the slice spacing changes during the acquisition. The correct way of interpolating from non-uniformly sampled data onto a uniform grid is the reverse of sinc interpolation. This methodology, sometimes used in k-space regridding (Robson et al 1997, Atkinson et al 2000), involves calculating the sinc coefficients to go from the desired uniform sampling points to the non-uniform locations acquired, and inverting the matrix of coefficients in order to do the correct interpolation. In the cases of 3D ultrasound and CT variable slice sample spacing, the data are a long way from being bandlimited, so the benefits of inverse sinc interpolation may be small in any case.
> 
> *Section 9.2 Interpolation during registration*
> 
> Many registration algorithms involve iteratively transforming image A with respect to image B while optimizing a similarity measure calculated from the voxel values. Interpolation errors can introduce modulations in the similarity measure with T . This is most obvious for transformations involving pure translations of datasets with equal sample spacing, where the period of the modulation is the same as the sample spacing (Pluim et al 2000). Figure 3 illustrates this effect. This periodic modulation of the similarity measure introduces local minima that can lead to the incorrect registration solution being determined.
> 
> The computational cost of ‘correct’ interpolation is normally too high for this approach to be used in each iteration, so lower-cost interpolation techniques must be used. There are several possible approaches. The first isl to use low-cost interpolation, such as trilinearornearest neighbour, until the transformation is close to the desired solution, then carry out the final few iterations using more expensive interpolation. An alternative strategy is to take advantage of the spatial-frequency dependence of interpolation errors. Trilinear interpolation low-pass filters the data, and therefore if the images are blurred prior to registration (high spatial frequency components are removed), the interpolation errors are smaller so errors in the registration are less. Although the loss of resolution that results from blurring is a disadvantage, the registration errors caused by the interpolation errors can be greater than the loss of precision resulting from blurring.
> 
> *9.3. Transformation for intermodality image registration*
> 
> It should be emphasized that these interpolation issues are more critical for intramodality registration where accuracy of considerably better than a voxel is frequently desired, than for intermodality image registration. In intermodality registration, one image is frequently of substantially lower resolution than the other, and the desired accuracy of the order of a single voxel at the higher resolution. Furthermore, it is common for the final registration solution to be used to transform the lower resolution image to the sample spacing of the higher resolution modality. Interpolation errors are still likely to be present if trilinear interpolation is used without care, and may slightly reduce the registration accuracy, or degrade the quality of the transformed images.

## Instructions

In this 10x mini project, pick an issues that was discussed in section 9, and dive into it in more detail.  In particular, create a python script that demonstrates that produces a nice visualization.

Here are some ideas:

- Explore how different forms of interpolation acts as a lowpass filter.
- Expand on why you can not do perfect interpolation using a sinc function on real world medical images.  Try to do "perfect" sinc interpolation by zero-padding the original image; compare this with a sinc interpolation applied with a window; try using different types of windows.
- Implement reverse sinc interpolation on non-uniformly sampled data.  Compare this with natural neighbor interpolation on the same data.
- Analyze the computational cost of tri-linear interpolation vs windowed sinc interpolation vs. any other commonly used forms of interpolation.  Explore GPU optimizations.
- Implement sinc interpolation on the GPU using PyOpenGl
- Any other cool idea you have!


## Example Script

I am going to upload a sample script with some "image generating functions" which we can use to more easily compare our interpolation results.
