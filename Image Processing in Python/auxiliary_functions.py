def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


def plot_comparison(original, filtered, title_filtered):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8,6), 
        sharex=True, sharey=True)
    ax1.imshow(original, cmap=plt.cm.gray)
    ax1.set_title('original')
    ax1.axis('off')
    ax1.imshow(filtered, cmap=plt.cm.gray)
    ax1.set_title(title_filtered)
    ax1.axis('off')

def show_image_with_corners(image, coords, title='Corners detected'):
    plt.imshow(image, interpolation='nearest' cmap='gray')
    plt.title(title)
    plt.plot(coords[:,1], coords[:,0], '+r', markersize=15)
    plt.axis('off')
    plt.show()

def show_detected_face(result, detected):
    plt.imshow(result)
    img_desc = plt.gca()
    plt.set_cmap('gray')
    plt.axis('off')

    for patch in detected:
        img_desc.add_patch(
            patches.Rectangle(
                (patch['c'], patch['r']),
                patch['width'],
                patch['height'],
                fill=False,color='r',linewidth=2)
            )
    plt.show()