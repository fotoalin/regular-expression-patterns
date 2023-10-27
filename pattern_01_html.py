"""
Extracting all matching patters from complex html content
and storing them in a list for further processing
"""
sample_content = """

                                            
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Mini Cheesecake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                            <span class="Polaris-Icon_yj27d">
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Brownies</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Carousel Cake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Merchandise</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Candles</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Animal Face Cake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> cheesecake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Brownie Box</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Posh Cake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Naked Cake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Shard Cake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Fantasy Cake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Layer Cake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Loaf</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Heart Cake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Party Cake</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                                <li class="tagItem">
                                                    <span class="Polaris-Tag_375hg Polaris-Tag--removable_1q527">
                                                        <span title="applied tag: Layer Cake" class="Polaris-Tag__TagText_lsfh6"> Brownie Boxes</span>
                                                        <button type="button" aria-label="remove tag: Layer Cake" class="Polaris-Tag__Button_r99lw" data-bs-placement="auto" title="remove tag: Layer Cake">
                                                            <span class="Polaris-Icon_yj27d">
                                                                <span class="Polaris-VisuallyHidden_yrtt5"></span>
                                                                    <svg viewBox="0 0 20 20" class="Polaris-Icon__Svg_375hu" focusable="false" aria-hidden="true">
                                                                        <path d="m11.414 10 4.293-4.293a.999.999 0 1 0-1.414-1.414L10 8.586 5.707 4.293a.999.999 0 1 0-1.414 1.414L8.586 10l-4.293 4.293a.999.999 0 1 0 1.414 1.414L10 11.414l4.293 4.293a.997.997 0 0 0 1.414 0 .999.999 0 0 0 0-1.414L11.414 10z"></path>
                                                                    </svg>
                                                                </span>
                                                        </button>
                                                    </span>
                                                </li>
                                            
                                            


                                        """


import re

pattern = r'<span title="applied tag:.*?" class="Polaris-Tag__TagText_lsfh6">\s*(.*?)\s*</span>'

matches = re.findall(pattern, sample_content)

names = []
for item in matches:
    item = item.strip()
    if item:
        print(item)
        names.append(item)

print(names)
