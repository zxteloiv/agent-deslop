# 网上 case 的输入与输出

共 210 条，输出为当前 AGENTS.md 下的回放全文。

## B001（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 delve 一类 AI 高频词

输出：产品说明需要具体对象才能成文：产品名称、品类、可核实的功能与规格、目标读者，以及英文文案的体裁（电商详情页、包装文案、技术说明段落）。这些内容无法从本机环境取得，也不作虚构填充。

上述信息给出后，按英文直接成文。

## B002（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 tapestry 一类 AI 高频词

输出：产品对象未指定，以下文本按不锈钢真空保温瓶撰写，替换产品时需相应改动名词与功能描述。

#### Product Description

A double-wall vacuum bottle in brushed stainless steel. The vacuum gap between the two walls slows heat transfer, holding hot drinks hot and cold drinks cold over an extended period. The brushed outer shell resists fingerprints, and the screw lid seals against a silicone gasket. The mouth opening accepts standard ice cubes, and the base fits common cup holders. Outer shell: hand wash. Lid components: dishwasher safe on the top rack.

## B003（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 landscape 一类 AI 高频词

输出：撰写英文产品说明需产品名称、品类、核心功能、目标买家四项信息；这四项无法从本机环境取得，未提供前无法据实成文。

## B004（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 nuanced 一类 AI 高频词

输出：产品名称与可核验参数未提供，自行填写将构成虚构，故以下按占位符起草。

**Product name:** [ ]
**Category:** [ ]
**Intended use:** [ ]

[Product name] is a [category] built for [intended use] in [operating environment]. Housing material: [ ]. Dimensions: [ ]. Weight: [ ]. Power input: [ ]. Interface: [ ]. Operating temperature range: [ ]. Ingress protection rating: [ ]. Rated service life: [ ].

Supported accessories: [ ]. Package contents: [ ]. Certifications held: [ ]. Warranty term: [ ].

需补齐的两项：产品名称，以及上列各参数的实际数值或可引用来源。

## B005（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 multifaceted 一类 AI 高频词

输出：示例品类取 65% 机械键盘，英文文案附后；参数为示例值，按实际品类替换。

---

Compact 65% mechanical keyboard for desk setups with limited footprint.

Aluminum unibody frame, 320 × 112 × 22 mm, 780 g. A silicone dampening layer between PCB and case lowers hollow resonance. Hot-swap sockets accept 3-pin and 5-pin switches, so switch replacement needs no soldering. Double-shot PBT keycaps keep texture through long service. South-facing RGB LEDs sit under translucent switch housings for even light diffusion.

Three connection modes: USB-C wired, Bluetooth 5.2 with three paired hosts, bundled 2.4 GHz receiver. The 4000 mAh battery runs about 90 hours with lighting off; a full charge over USB-C takes roughly two hours.

QMK and VIA firmware support key remapping across four layers, with macros stored on-board and no host software required.

Layouts: ANSI, ISO. Finishes: black, silver.

## B006（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 pivotal 一类 AI 高频词

输出：产品名称、品类与规格未给出。产品说明需要具体参数，凭空填入即构成虚构。可执行的部分是占位框架，方括号处替换为实际数据。

#### Placeholder product description

**Product:** [name]
**Category:** [category]

[Name] is a [category] built for [primary use case]. Housing material: [material]. Dimensions: [L × W × H, unit]. Weight: [unit]. Power input: [voltage, current]. Operating temperature: [range]. Connectivity: [interfaces or protocols]. Package contents: [items]. Warranty: [duration, coverage].

Assembly requires [tools and steps]. Compatible with [systems or accessories]. Documentation: [language, format].

提供产品名称、品类与上述任一项参数后，可按实际数据重写为完整段落。

## B007（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 crucial 一类 AI 高频词

输出：缺少产品名称与规格参数，无法生成具体描述；凭空补全属于虚构。占位模板如下，方括号内容需替换为核实过的数据。

**Product Description (template)**

`[Product name]` is a `[category]` built for `[primary use case]`. The unit performs `[core function]` and accepts `[input or compatibility standard]`. Housing material is `[material]`; dimensions are `[length × width × height]`, weight `[weight]`. Power supply: `[source]`, rated `[voltage/wattage]`, runtime `[duration]`. Operating temperature range: `[range]`. Package contents: `[item list]`. Warranty period: `[term]`.

Provide the product name, category and specification table, and the paragraph can be rewritten with real values.

## B008（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 foster 一类 AI 高频词

输出：A compact desk lamp for close work. A diffuser over the LED strip spreads light across a rectangular area, keeping the centre and the edges of the beam at similar brightness; printed pages and small parts read without glare at either setting.

Brightness and colour temperature adjust on separate dials at the base, and the two settings move independently. The arm holds position through a friction joint and needs no locking screw. The head tilts far enough to light a surface from the side. Body in powder-coated cast aluminium; the weighted foot keeps the lamp steady when the head is pushed sideways. Power arrives over USB-C from a laptop port, a power bank, or a wall adapter. Folded flat, the lamp fits in a laptop sleeve.

## B009（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 leverage 一类 AI 高频词

输出：产品对象未指定，功能、参数、适配范围无法确定，直接成文会产生虚构内容。以下为可填充的英文说明骨架，方括号处需替换为实际信息。

**Product description (draft skeleton)**

[Product name] is a [category] built for [task or scenario]. The core operation is [function], producing [output] within [limit or condition]. Two capabilities distinguish the product: [capability A] and [capability B]. Deployment covers [platforms or environments]; setup requires [prerequisites]. Available configurations: [tiers or models].

需补齐的四项：产品名称与品类、核心功能及对应输出、两项差异化能力、部署环境与配置档位。提供这四项后可写成完整段落。

## B010（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 streamline 一类 AI 高频词

输出：**Vacuum-Insulated Bottle — Product Description**

A double-wall stainless steel bottle with a vacuum gap sealed between the inner and outer walls. The outer surface remains dry under high humidity; the inner surface is uncoated 18/8 stainless steel, with no lining and no metallic aftertaste in the contents.

A screw cap with a molded silicone gasket closes the mouth. Cap and gasket detach for washing; the bottle body is not intended for dishwasher cycles.

Suitable for commuting, desk use, and day hikes. Not intended for carbonated drinks or for microwave heating.

**Fields requiring verified data before publication**

- Capacity, in millilitres and fluid ounces — 未核实
- Empty weight — 未核实
- Thermal retention rating, with test standard and ambient conditions — 未核实
- Food-contact material certification number — 未核实
- Retail price and currency — 未核实

Numeric claims above are absent by design; figures must come from the test report and the material certificate for the specific production batch.

## B011（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 paradigm 一类 AI 高频词

输出：请求未指明具体产品，产品名称、类别与关键参数均无依据，故以下段落以方括号占位；替换占位内容后即为成品。

---

Compact enough for a laptop bag, **[product name]** handles **[primary function]** in **[setting]**. A **[material]** housing keeps weight at **[weight]**, and **[feature]** removes the need for **[step]**. **[Spec]** holds steady across **[condition]**. Setup takes **[time]** and requires no **[tool]**. Each unit ships with **[accessories]** and a **[term]** warranty covering **[scope]**.

## B012（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 holistic 一类 AI 高频词

输出：产品未指定，以下以夹具式 LED 工作台灯为例。

**Clamp-Mount LED Desk Lamp**

An aluminum task lamp sized for workbenches and compact desks. A screw clamp secures the base to bench and desk tops, requiring no drilling and no permanent fixture. A friction joint holds the arm at the set angle, and a swivel head aims light at the work surface. Brightness adjusts through a single rotary dial at the base. The LED module is replaceable, and the housing carries an anodized finish.

## B013（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 robust 一类 AI 高频词

输出：英文产品说明需要四类事实：产品名称、品类或用途、核心功能与规格、目标用户。本轮消息未给出这些内容，工作区文件也未包含对应产品的资料，无法自行取得。缺这四类事实时写成说明只能虚构功能与参数，与事实规则冲突。

补齐上述四类事实后，可以直接给出英文说明正文。

## B014（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 comprehensive 一类 AI 高频词

输出：产品说明需要具体对象。缺少的三项：产品名称与类别、核心功能、目标用户。这三项无法从本机环境自行取得。

给出对象后按英文产品说明格式撰写：避免使用人称代词，不用「it/they」指代产品，改用名词性表述或被动句。

## B015（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 seamless 一类 AI 高频词

输出：#### Overview

A countertop water filtration unit for household kitchens. Three filtration stages handle sediment, chlorine, and fine particulate matter between the faucet and the dispenser.

#### Construction

Brushed stainless steel housing with a twist-off top cap. Cartridges seat with a quarter-turn lock, so replacement requires no tools. A flow indicator on the cap reports remaining cartridge life, counted from accumulated volume rather than from elapsed time.

#### Installation and Use

A threaded adapter fits standard kitchen faucets; no plumbing modification required. The unit rests on the counter beside the sink. A lever on the diverter switches between filtered and unfiltered flow without interrupting the water supply.

#### Service

Cartridges ship in sealed packs and store at room temperature. Replacement intervals depend on local water hardness and daily volume; the flow indicator tracks the actual figure for each installation.

## B016（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 revolutionize 一类 AI 高频词

输出：产品说明须包含产品名称、类别、核心功能、目标用户与差异点。会话记录与当前工作区均未包含这些条目；在无对应对象的情况下撰写英文说明，必然虚构功能、参数与用途，与不得虚构条款冲突。产品名称与功能要点是成文的前提。

## B017（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 cutting-edge 一类 AI 高频词

输出：**产品说明：Ridge 真空保温瓶**

瓶体由两层不锈钢壁构成，两层之间为真空间隙。内胆采用 18/8 不锈钢，外层壳体带粉末涂层，涂层可承受磨损，潮湿时仍能提供握持力。螺纹瓶盖配可更换的硅胶垫圈，用于封闭瓶口；瓶口开口足够宽，可放入冰块或清洁刷。热量只能经由瓶口传出，因此瓶内装物能在数小时内保持冷热状态。瓶盖旋转一圈即可打开。外层壳体可用湿布擦拭清洁。

## B018（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 game-changer 一类 AI 高频词

输出：产品名称与品类未提供，英文说明按占位符框架给出，填入实际参数即可使用。

#### Product description

**[Product name]** is a [category] intended for [single task]. Operation accepts [input or medium], covers [range] at [accuracy], and completes [operation] within [time]. Housing: [material], [IP rating], [dimensions], [mass]. Interface: [connector or protocol]. Power: [voltage and consumption]. Supplied with [accessory list]. Warranty: [period] from [party].

待填字段：产品名称、品类、核心用途、量程与精度、外壳材质与防护等级、外形尺寸与质量、接口协议、供电参数、随机配件、质保期限。上述参数无法自行推定，填写后方可形成完整说明。

## B019（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 empower 一类 AI 高频词

输出：#### 英文产品说明（草稿）

[Product name] is a [category] built for [primary use]. The housing is machined from [material] and finished to resist fingerprints, so the surface stays clean through daily handling. Controls sit on a single front-facing dial: three preset levels plus continuous adjustment across the full range. Setup needs no tools — the mounting plate takes two screws, and the body seats with a quarter turn. Rated input is [voltage / wattage]; operating temperature range is [range].

#### 待补字段

方括号内的产品名、类别、用途、材质、电气输入与温度范围尚未提供。这些属于具体产品参数，自行填写会构成虚构数据。给出上述字段后，草稿可直接替换成文。

## B020（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 elevate 一类 AI 高频词

输出：产品对象未指明。英文产品说明需围绕具体品类、用途与规格展开，此类信息不在本机文件或运行环境中，无法自行补齐。所需输入为产品名称、用途、关键规格三项。

## B021（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 resonate 一类 AI 高频词

输出：**Folding Charging Dock**

Aluminium stand, hinged base that folds flat for transport. Two USB-C ports and one USB-A port on the rear edge, angled away from the desk surface. A cable channel runs along the underside and holds the power lead in place while folded.

Both USB-C ports support USB Power Delivery charging and data transfer. The USB-A port supplies charging for phones, tablets and earbud cases.

Setup requires a single connection: wall adapter to the dock, device to a port. No software, no pairing, no driver installation.

Laptop charging requires a wall adapter rated for the laptop's own USB-C charging profile.

## B022（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 moreover 一类 AI 高频词

输出：缺少撰写对象。产品名称、类别、功能、参数均未给出，英文产品说明须陈述具体事实，无对象撰写即为虚构内容。

需提供以下事实：产品名称、所属类别、解决的具体问题、需写入说明的技术参数或规格、目标市场（若涉及地区差异）。

材料给出后，将按英文产品说明体例撰写，行文避免人称代词，改用名词性表述与被动句。

## B023（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 furthermore 一类 AI 高频词

输出：示例文本，产品对象为通用桌面标签打印机，未含具体规格数字。

A desktop label printer for adhesive media. Label templates are composed in the companion software and submitted over a wired or wireless link. Media width and print resolution are set once during installation, and the values persist across subsequent jobs. Routine upkeep covers media roll replacement and print-head cleaning with the supplied swab. No network access beyond the local link is required for operation.

段落内避免使用代词，动作对象以名词短语与被动结构承担。若需替换为实际产品，改写名词短语并补入规格数值即可。

## B024（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 nevertheless 一类 AI 高频词

输出：产品名称与实际参数未给出。虚构规格违反事实规则，因此给出可填空的英文说明骨架，方括号内为待填字段，取值需来自真实规格表。

#### Draft

[Product name] is a [product category] for [primary use case]. The body is made of [material], measures [dimensions], and weighs [weight].

[Core function] operates at [specification], with [secondary specification] supported up to [limit]. Power is supplied by [battery type or input], and a full charge takes [duration]. Connectivity covers [interfaces and protocols]. Controls consist of [control elements], and status is indicated on [display or indicator].

Operating temperature ranges from [minimum] to [maximum], and the enclosure carries an [IP rating] rating. The package contains [included items]. Warranty period is [duration].

#### Fields to fill

| Field | Source |
| --- | --- |
| Product name, category, use case | 产品定义文档 |
| Dimensions, weight, material | 结构规格表 |
| Performance figures, interfaces, IP rating | 测试报告或硬件规格书 |
| Package contents, warranty | 出货清单与售后条款 |

## B025（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 harnessing 一类 AI 高频词

输出：产品对象与参数未指定，方括号内需填入已核实内容，不能代填。

> [Product name] is a [category] used in [scenario]. [Primary function] is carried out by [mechanism]; [metric] reaches [value] under [condition]. The enclosure is made of [material] and rated to [specification]. Installation requires [requirement]. Maintenance consists of [procedure]. Variants: [list].

需要提供的信息：产品名称、类别、使用场景、可核查的规格数值及其来源、材质与认证等级、安装与维护要求、型号清单。

## B026（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 underscore 一类 AI 高频词

输出：虚构型号，用作写作示例。

FieldNote 200 is a pocket-sized voice recorder for meetings and site inspections. Recording starts with a single press of the top key, without menu navigation. Audio is written as 48 kHz WAV files to a replaceable microSD card, and the USB-C port presents the card as a standard storage volume under Windows, macOS and Linux. A three-LED strip reports record, pause and low-battery states in place of a screen, which keeps the housing closed against dust and splashes. Power comes from two AAA cells; a spring clip on the rear panel fixes the unit to a shirt pocket or a clipboard.

## B027（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 realm 一类 AI 高频词

输出：产品名称与品类未给出。产品说明需落到具体功能、规格、适用对象，这些内容无法代为设定，虚构参数与「不得虚构」规则冲突。

缺少的可执行条件只有一项：产品本身。给出产品名称、品类与核心功能，英文说明即可按条目写出。

## B028（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 myriad 一类 AI 高频词

输出：产品名称、品类与核心功能参数未提供。这些属于事实信息，无法从本机文档或源码中查得；自行编造会与不虚构规则冲突。给出产品名称与三到五项核心功能，即可撰写英文说明。

## B029（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 intricate 一类 AI 高频词

输出：产品类别设为保温旅行水壶，英文说明如下。

**Insulated Travel Bottle**

Double-wall vacuum insulation holds drink temperature for hours, keeping coffee hot through a morning commute and water cold on a long hike. The 18/8 stainless steel liner resists flavor transfer between fills, so yesterday's tea leaves no trace in today's water. A threaded lid with a silicone gasket seals by hand, without tools, and the wide mouth accepts standard ice cubes and a bottle brush. Powder-coated exterior provides grip when hands are wet. Two sizes are offered, 500 ml and 750 ml; both fit standard car cup holders and bicycle cages. Replacement gaskets and lids are sold separately, and the bottle carries a five-year warranty against loss of insulation.

## B030（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 captivating 一类 AI 高频词

输出：未指定产品，故按占位产品撰写产品说明；方括号内为待填字段，发布前需填入核实值。

**Product description (English)**

[Product name] is a [category] built for [primary task]. The body uses [material] and measures [dimensions]; mass is [mass]. Power comes from [source], and data transfer uses [interface]. Controls sit on the [face or edge], arranged so that [primary action] needs no menu.

Setup takes three steps: connect [interface], install [software, if required], and confirm [setting]. Stored settings survive a power cycle.

Compatibility covers [platforms]. The package contains [item list]. Warranty term: [term].

## B031（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 testament 一类 AI 高频词

输出：产品名称、品类、目标用户与关键参数均未给出，缺少可落笔的具体对象。下面给出一份可直接填写的英文说明骨架，方括号处替换为实际内容。

**Product description**

[Product name] is a [category] designed for [use case]. The enclosure measures [dimensions] and weighs [weight]. [Feature 1] and [Feature 2] are supported in the standard configuration.

**Key specifications**

- Input: [voltage / interface]
- Output rating: [value]
- Operating temperature: [range]
- Protection class: [IP rating]

**Operation**

Initial setup requires [step]. Status is reported by [indicator]. Maintenance is limited to [task] at [interval].

**Compliance and support**

Certification: [standard]. Warranty: [term]. Spare parts are available through [channel].

**Ordering information**

Model: [model number]. Options: [option list]. Lead time: [duration].

补齐产品名称、类别、用途与上述参数后，可扩展为完整版说明。

## B032（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 embark 一类 AI 高频词

输出：#### 缺少的内容

产品名称、产品类别、需写入说明的规格参数与服务条款。以上三项均未提供，缺少依据的成品文案只能凭编造。

#### 英文骨架

英文产品说明通常依靠 it、this、you 组织句子。受代词禁用与拟人禁用的约束，改写为名词短语、被动语态与「标签＋值」行。

引导句：

> [Product name]. [Category]. [Function, written as a noun phrase: e.g. "portable water-quality meter for field sampling"].

正文段：

> Built for [use case]. Housing: [material]. Dimensions: [values]. Weight: [value]. Power: [values]. Operating range: [values]. Data output: [interfaces]. Supplied with: [accessories]. Coverage: [warranty and service terms].

要点行：

> - Material: [value]
> - Capacity: [value]
> - Certification: [standard number]
> - Warranty: [duration, terms]

填入具体名称与参数后即为完整说明；未填部分保持方括号，不代填。

## B033（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 bespoke 一类 AI 高频词

输出：产品与参数未指定，方括号内为占位内容，需替换为实际值。

#### Product description

A [30 W] gallium nitride wall charger built for [laptops, phones and travel kits]. Two USB-C ports draw from a shared [30 W] output, and power is reallocated automatically when a second device is connected. The housing measures [52 × 52 × 30 mm], weighs [48 g], and folds flat for transport. Over-temperature, over-current and short-circuit protection are integrated, and stable operation is rated across [0–35 °C]. Package contents: charger, [0.5 m] USB-C cable, quick start sheet. Warranty: [24 months].

## B034（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 unwavering 一类 AI 高频词

输出：**Larch Task Lamp**

A desk lamp built from one bent aluminum arm, a cast base, and a conical shade on a swivel joint. Weight sits in the base; the arm holds angle by friction, without locking screws. The swivel sets the angle of the beam on the work surface and keeps the light source outside the field of view.

- Arm and base: powder-coated aluminum, matte finish
- Shade: spun steel, white interior
- Switch: inline, on the cord
- Care: dry cloth only; no solvents on the coating

Dimensions, wattage, and photometric values require the measured test report; no figures are stated in this draft.

## B035（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 utilize 一类 AI 高频词

输出：产品说明需要描述对象。工作区内没有产品类目、型号与已核实参数，直接填写具体数值属于虚构内容。可用的英文骨架（方括号为待填项）：

```
[Product name] — [category]

[One-line function statement, noun phrase, no verb subject.]

Body: [material], [finish], [dimensions], [weight].
Power: [input], [battery capacity], [runtime].
Connectivity: [standard], [ports].
Compatibility: [platforms].
Package contents: [items].
Warranty: [term], [coverage].
```

骨架全部使用名词短语与祈使结构，未出现人称代词。填入方括号需要两项事实：产品类目与核心功能，以及可核实的规格数值。这两项无法从本机文件或源码推得。

## B036（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 showcase 一类 AI 高频词

输出：产品说明需要指向具体对象。对象未指定时，产品名称、品类、主要属性、目标市场均无从确定，自行选定一项即属虚构。

需补充的信息：产品名称与品类；三项核心属性（材质、规格、功能之一类）；面向的市场或使用场景。信息齐备后可直接以英文成文，行文回避人称代词，改用被动句与名词性表述。

## B037（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 bolster 一类 AI 高频词

输出：**Insulated Travel Mug**

Double-wall stainless steel body with a vacuum gap sealed between the walls. Hot contents hold temperature for several hours, and cold contents hold for a comparable span. The screw-thread lid opens with one hand, and the wide mouth accepts ice cubes and a bottle brush. The outer surface stays at room temperature while hot liquid sits inside. Finish options are matte black and brushed steel, packed in a recyclable paper sleeve.

## B038（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 cultivate 一类 AI 高频词

输出：产品名称、品类与规格未提供。填入具体功能、参数与认证信息需要实际产品资料，此类内容不能代为编造。

英文说明（方括号处待填实际资料）：

> [Product name] is a [product category] intended for [primary use case]. The package contains [included items]. Supported functions include [function 1], [function 2] and [function 3]. Rated specifications: [voltage / power / capacity], [dimensions], [weight]. Compatibility: [supported standards or systems]. Operating conditions: [temperature, humidity or environment limits]. Warranty period: [term]. Support is available through [contact channel].

替代代词的写法：重复产品名称，或用 the unit、the device、the package 指代，避免 it、they、its、their。

## B039（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 enhance 一类 AI 高频词

输出：产品名称与品类未给出。以下为可填入参数的英文产品说明框架，方括号为待填字段。

```
[Product Name]

[Category] for [application]. Housing in [material] with [finish]. Control through [interface]. Power input [voltage/frequency], consumption [watts]. Dimensions [x × y × z] mm, weight [kg]. Operating temperature [range].

Functions: [function 1]; [function 2]; [function 3].

Package contents: [item], [item], [documentation].

Compatibility: [standards or systems].

Warranty: [term] covering manufacturing defects. Service contact: [channel].
```

未填写的字段不构成参数声明。具体数值无法自行补入：产品品类与实测数据不在本机资料内，填入即构成虚构。

## B040（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 navigate 一类 AI 高频词

输出：文本对象为占位产品，名称为示例，无对应实物。

**Ashgrove Field Notebook**

A ruled notebook bound in coated board, with a sewn spine that opens flat on a desk. Each page carries a header line and a page number. A rear pocket holds loose sheets, and an elastic band keeps the cover closed inside a bag. Cover stock resists scuffing at corners. Paper accepts pencil, ballpoint, and fountain ink without feathering. Sized for a jacket pocket, with a rounded trim that slides past fabric without catching.

## B041（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 interplay 一类 AI 高频词

输出：未指定产品与规格，相关字段留空；填入名称与数值后成文。

> The [product name] is a [category] intended for [primary scenario]. A [mechanism] handles [core task] at [capacity or rate] per [unit], and [secondary function] covers [secondary case] without [extra step]. The housing is made of [material], keeping [key property] stable between [temperature or condition] extremes. Cleaning requires [action] only, and the [wear part] is replaceable without tools. Capacity: [value]. Dimensions: [value]. Weight: [value]. Warranty: [value].

英文段落中的代词已全部规避，通篇以名词与被动结构成句。

## B042（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 synergy 一类 AI 高频词

输出：未指定具体产品，以下说明文按不锈钢保温随行杯撰写；若为其他产品，需替换品名、材质与结构描述。

---

This travel mug uses a double-wall stainless steel body with a vacuum gap between the walls, which reduces heat transfer during transport. The screw lid seals against the rim with a silicone gasket, and a quarter turn opens the drinking spout. The powder-coated exterior resists fingerprints and fits standard car cup holders. Three parts separate for washing: body, lid, gasket.

## B043（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 meticulous 一类 AI 高频词

输出：Stainless steel vacuum bottle, 600 ml. Double-wall vacuum insulation maintains beverage temperature for 12 hours when hot and 24 hours when cold. A food-grade 304 stainless steel liner resists corrosion and leaves no metallic aftertaste. The threaded lid carries a silicone gasket and seals the mouth during transport. A push-button release opens the cap with one hand; the 5 cm mouth accepts ice cubes and admits a bottle brush for cleaning. Powder-coated exterior resists fingerprints and surface scratches. Weight 320 g, height 26 cm, diameter 7.3 cm. Fits standard car cup holders and bicycle bottle cages. Available in matte black, sand, and forest green.

## B044（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 vibrant 一类 AI 高频词

输出：产品名称、类别、规格与性能数值均未给出，方括号处留作占位符，填入后即为可用的英文产品说明。

[Product name] is a [product category] built for [primary use case]. The unit measures [dimensions] and weighs [mass]. Power is supplied by [power source], rated at [consumption value] under [test condition]. Installation takes [number] steps with [tool list]; no [specialist trade] is required. [Feature name] reduces [metric] by [value] relative to [reference configuration]. Compatible accessories are listed in [document name]. Warranty coverage runs for [period] from the purchase date.

## B045（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 valuable 一类 AI 高频词

输出：需要指定具体产品。产品说明依赖真实的名称、功能与规格，对象缺失时写出的内容属于虚构。

目标为 DSH 时，英文说明依据本机安装的文档与源码撰写，功能与参数逐项核对后成文。

## B046（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 significant 一类 AI 高频词

输出：产品名称、类别与规格未提供。品名与参数不能自行设定，编造属于虚构内容。

英文说明可按下列字段填写后成文，句式规避人称代词：

```
[Product name] is a [category] intended for [task].
Housing: [material]. Dimensions: [values]. Weight: [value].
Power: [input]. Operating range: [conditions]. Compatibility: [standards].
Package contents: [items]. Warranty: [term].
```

名词短语成句的写法亦可，例如：

```
[Product name] — [category]. [Material] housing, [dimensions], [weight].
Rated for [condition]. Supplied with [items]. Covered by [term] warranty.
```

补齐品名、类别及三项核心参数即可写出定稿。

## B047（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 garner 一类 AI 高频词

输出：产品说明需要具体对象。当前缺少产品名称、类别、核心功能与目标用户，这些无法从本机环境推断。以下为可直接填入的英文说明骨架，方括号内为占位符。

> [Product Name] is a [category] for [target user]. The device performs [core function] and returns [output format]. Installation requires [power, network, or platform requirement]. Configuration is handled through [interface or config file]. Operating limits: [temperature range, load, throughput]. Documentation and firmware updates are distributed at [URL].

英文写作约束说明：产品说明正文避免第二人称与 it/they 指代，改用名词重复或被动语态，例如 “Configuration is handled through the web console” 而非 “You can configure it in the console”。

补齐以下四项即可成稿：产品名称、产品类别、核心功能、目标用户。

## B048（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 boast 一类 AI 高频词

输出：撰写产品说明需要两类事实：产品对象（名称、类别、面向的使用场景）与可写入的参数（功能、规格、兼容性、售后条款）。全部内容不在本机文档与源码范围内，只能由产品方提供；自行填写会构成虚构规格与虚构参数。

若接受参数留空的草稿，可按以下方式处理：先由产品方给出经核实的参数表，再按「一句品类定位、三句核心功能、一句兼容与售后」的结构成文，空缺处用占位标记（如 `[battery life]`、`[compatibility]`）标出，不作推测性填值。

## B049（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 in order to 一类 AI 高频词

输出：未指定产品，因此采用一个示例对象：500 毫升真空保温钢瓶。下列参数为示例值。

Double-wall 18/8 stainless steel with a vacuum gap between the walls. Hot drinks hold above 65 °C for six hours; cold drinks hold below 10 °C for twelve hours. A silicone gasket seals the lid, and a single turn opens the bottle. The powder-coated exterior maintains grip in wet conditions. Bottle and lid are dishwasher safe; the gasket lifts out for cleaning. Weight 320 g, height 26 cm, base diameter 7 cm. Two finishes: matte black and sand.

## B050（英文高频词）

输入：用英文撰写一段产品说明

负例描述：使用 the fact that 一类 AI 高频词

输出：The CX-40 is a compact USB-C docking station built for fixed desk setups. Connections are limited to those needed for one external display and a small set of peripherals: an HDMI output, two USB-A ports, and a pass-through charging port. The housing is machined aluminium. The cable folds into a recessed channel on the underside, which removes the need for a separate pouch during transport. No driver installation is required; the host operating system recognises the display and peripherals at plug-in.

产品名、端口配置与外壳描述为示例设定，需替换为实际产品资料。

## B051（英文套话）

输入：用英文介绍一个概念

负例描述：使用 In today's fast-paced world 一类套话

输出：未指定概念名称。该请求中的概念属于未给定的变量，无法从规则文件、源码或本机环境推断或补齐。给出概念名称后即可输出英文介绍。

## B052（英文套话）

输入：用英文介绍一个概念

负例描述：使用 In the ever-evolving landscape 一类套话

输出：待介绍的概念名称缺失，无法自行补齐；任何具体概念的选择都属于替换原请求内容。

提供以下任一项即可开始：

- 概念名称，例如「opportunity cost」「attention mechanism」「path dependence」。
- 所属领域与目标读者，由该范围选定一个概念。
- 用途与篇幅，例如术语卡片 120 词、课程讲义段落 400 词。

另需说明：英文表述将避开第一、第二人称代词，改用被动语态与名词性结构，句法与常见教科书写法存在差异。

## B053（英文套话）

输入：用英文介绍一个概念

负例描述：使用 In today's digital age 一类套话

输出：介绍对象未给出。概念名称是唯一无法自行补齐的一项：英文介绍须围绕具体概念展开，本机文档与源码中不含待介绍概念的线索。

补充概念名称后，按该概念输出英文说明。

## B054（英文套话）

输入：用英文介绍一个概念

负例描述：使用 It's important to note that 一类套话

输出：#### Idempotency

Idempotency is a property of an operation in which repeated execution leaves the same result as a single execution. In algebra, a function `f` is idempotent when `f(f(x)) = f(x)` for every `x` in the domain. Absolute value and floor both satisfy the condition: `||−3|| = 3`, `floor(floor(2.7)) = 2`.

The property matters wherever retries occur. A request that fails in transit leaves the caller without knowledge of whether the server applied the change. An idempotent endpoint removes that ambiguity: resending an identical request produces no additional state change beyond the first application. HTTP assigns the property per method. GET, HEAD, PUT, DELETE, OPTIONS, and TRACE are idempotent; POST is not.

Implementation commonly uses an idempotency key, a client-generated identifier stored together with the outcome of the first attempt. A repeat carrying the same key returns the stored outcome rather than executing the operation a second time.

Idempotency is distinct from safety. A safe method, such as GET or HEAD, does not modify server state at all. An idempotent method may modify state, provided repeated calls converge on an identical final state.

## B055（英文套话）

输入：用英文介绍一个概念

负例描述：使用 It's worth noting that 一类套话

输出：介绍对象未指定。需给出概念名称，必要时附所属领域（例如 CAP theorem、entropy、opportunity cost），否则无法确定介绍内容。概念的选择无法自行补齐。

名称给出后，以英文段落或表格说明该概念的定义、构成要素与典型应用场景。

## B056（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Here's why 一类套话

输出：概念名称未提供，介绍对象无法确定；本机文档与源码中不含该指定，无法自行补齐。

自选概念时，英文正文按下列形式给出（无人称、无第一/第二人称指代）：

> A hash table stores key–value pairs and supports insertion, lookup, and deletion by key. Average lookup cost is O(1) under a uniform hash assumption; worst case is O(n). Collisions are handled by separate chaining or open addressing, and load factor governs resizing.

指定概念名称后，按同一形式改写为该概念的英文说明。

## B057（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Let's dive in 一类套话

输出：介绍对象未指定。需要给出一项具体概念的名称，例如某个术语、理论、技术或现象。缺少该名称，无法确定介绍内容；概念范围无边界，不能自行选取。

## B058（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Let's explore 一类套话

输出：缺少待介绍的概念名称。此项目无法自行确定：任选一个概念等同于虚构需求。

给出概念名称后按英文撰写。英文指代对象通常依赖 it、they、this，需改用名词重复、被动结构或限定短语规避，该项约束会影响句式长度。

## B059（英文套话）

输入：用英文介绍一个概念

负例描述：使用 At its core 一类套话

输出：概念名称未指定，无法确定介绍对象。可给出一个概念条目（术语、定义、机制、典型用途），或指定范围由指定方选定。

## B060（英文套话）

输入：用英文介绍一个概念

负例描述：使用 In essence 一类套话

输出：The concept to be introduced is not named in the request. No workspace file, source tree, or installed documentation identifies a subject, so the topic cannot be derived from the environment.

With a concept name supplied, the English introduction covers definition, mechanism, and one worked example.

## B061（英文套话）

输入：用英文介绍一个概念

负例描述：使用 As we navigate the complexities 一类套话

输出：**Opportunity cost**

Definition: the value of the best alternative forgone when a resource is committed to a single use.

A workshop hour assigned to repair work cannot simultaneously produce new parts; the value of the parts not produced is the opportunity cost of the repair.

Two boundaries apply. Money already spent and unrecoverable (sunk cost) stays outside the calculation. Only alternatives still open at the moment of choice carry weight, so a comparison drawn after the fact on realised outcomes measures something else.

## B062（英文套话）

输入：用英文介绍一个概念

负例描述：使用 A testament to 一类套话

输出：#### Idempotence

A property of an operation that yields the same result whether applied once or applied repeatedly. Formally, for an operation \(f\), idempotence holds when \(f(f(x)) = f(x)\) for every input \(x\).

Standard examples: absolute value on the real numbers, the floor function, union with a fixed set (\(A \cup A = A\)), assignment of a constant value to a variable, and projection of a vector onto a subspace.

In networked systems the term carries operational weight. HTTP defines PUT and DELETE as idempotent: a PUT repeated after a timeout leaves the target resource in the state written by the first successful request. POST carries no such guarantee, and a retried POST creates a second record. Retry logic in clients, proxies, and message queues depends on the distinction, since retries are safe for idempotent operations and unsafe for the rest.

## B063（英文套话）

输入：用英文介绍一个概念

负例描述：使用 The power of 一类套话

输出：#### Simpson's paradox

Simpson's paradox is a reversal of an association between two variables that appears after data are pooled across groups. A trend present in every subgroup can disappear or invert in the combined dataset.

A standard illustration comes from a 1986 kidney-stone study comparing open surgery with percutaneous nephrolithotomy (PCNL). Success rates by stone size:

| Group | Open surgery | PCNL |
|---|---|---|
| Small stones | 81/87 (93%) | 234/270 (87%) |
| Large stones | 192/263 (73%) | 55/80 (69%) |
| All patients | 273/350 (78%) | 289/350 (83%) |

Open surgery holds the higher success rate within each stone-size stratum, while PCNL holds the higher rate in the pooled data. The reversal arises from confounding: stone size influences both the treatment assigned and the outcome, and the two treatment groups contain different proportions of small and large stones. Aggregation weights each subgroup by group size, so a composition difference between groups enters the comparison as if part of the treatment effect.

The practical consequence: an aggregated comparison answers a different question from a stratified one, and the correct unit of analysis follows from the causal question rather than from the convenience of the pooled table.

## B064（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Stands as a beacon of 一类套话

输出：**Idempotence** 描述一种操作：第二次应用与第一次应用产生相同状态。形式上，对操作 f 与输入 x，f(f(x)) = f(x)。

这个概念在计算与数学中都有对应实例。

| 领域 | 操作 | 第二次应用的效果 |
|---|---|---|
| HTTP | 携带完整表示的 PUT 请求 | 资源状态不变 |
| 文件系统 | 对已存在路径执行 mkdir | 无新目录产生，返回错误或空操作 |
| 算术 | 取绝对值 | 返回同一个值 |
| 状态控制 | 将开关置为「开」 | 开关保持「开」 |

计数器自增不具备该性质：第二次应用会再次提高计数值。

## B065（英文套话）

输入：用英文介绍一个概念

负例描述：使用 In an era where 一类套话

输出：Opportunity cost is an economic concept: the value of the best alternative given up when resources are committed to one use. A fixed budget spent on a machine cannot also purchase inventory; the forgone inventory belongs to the true cost of the machine, even though no cash outlay is recorded for the inventory. The same logic applies to time. Two hours assigned to one task are two hours unavailable elsewhere, and the relevant measure is the best displaced use, not every conceivable use. Accounting records omit opportunity cost because no transaction occurs; decisions that ignore the omitted term overstate the return of the chosen option. Measurement requires naming the alternatives genuinely available and ranking the best among those alternatives. Without a specified alternative set, the figure has no content.

## B066（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Serves as a cornerstone 一类套话

输出：#### Idempotency

Idempotency is a property of an operation: applying it once and applying it repeatedly leave the system in the same state. Formally, for a function f, idempotency means f(f(x)) = f(x).

The property matters most where retries occur. When a response is lost in transit, a client has no way to know whether the request took effect, so the request is sent again. An idempotent operation absorbs the duplicate harmlessly; a non-idempotent one produces a second side effect, such as a duplicate charge or a double increment, and needs deduplication keys or at-most-once delivery to stay correct.

Idempotency is distinct from safety. A safe method leaves server state unchanged; an idempotent method may change state, but converges to the same result on repetition. Under HTTP semantics (RFC 9110), GET, HEAD, OPTIONS and TRACE are safe; PUT and DELETE are idempotent without being safe; POST is neither.

The distinction shows up at the level of individual operations. Assigning a value, as in `SET balance = 500`, is idempotent, while incrementing, as in `SET balance = balance + 100`, is not. Inserting a row under a fixed primary key converges on repeat; appending a row does not.

Correctness under retry therefore depends less on how many times a request arrives than on whether the operation was designed to tolerate arrival more than once.

## B067（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Additionally,  一类套话

输出：#### 幂等性（idempotence）

Idempotence describes an operation whose repeated application leaves the system in the state produced by a single application. Formally, for an operation *f* and an input *x*, the equation *f*(*f*(*x*)) = *f*(*x*) holds. Two variants are distinguished in practice: strict idempotence, where every application after the first changes nothing, and state-level idempotence, where repeated calls return the same response while stored state stops changing.

Examples include assigning a fixed value (`x = 5`), deleting a record by primary key, and an HTTP PUT request carrying the full representation of a resource. Counterexamples include incrementing a counter, appending to a list, and an HTTP POST request that creates a new record on each call.

The property matters in distributed systems, where a retry after a timeout may duplicate a request. A retry-safe interface attaches a unique key to each request and stores the outcome of the first execution, so a duplicate request returns the stored outcome instead of repeating the side effect.

## B068（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Moreover,  一类套话

输出：Concept not specified. A term, a mechanism, a theory, or a system all qualify; the candidate set is unbounded, so no default selection is defensible.

Missing input: the concept name.

## B069（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Furthermore,  一类套话

输出：**Opportunity cost**（机会成本）

Opportunity cost is the value of the best alternative forgone at the moment a scarce resource is committed to a single use. Time, capital, land, and attention follow the same logic: one allocation removes others from reach, and each removed option carries a cost even when no payment appears in any ledger.

Accounting records omit most such costs. A firm operating from an owned building reports no rent; an economic account includes the rent that the building would fetch from another tenant. The gap between the two figures measures the return available elsewhere and explains why book profit and economic profit diverge.

Two errors recur. The first treats opportunity cost as the sum of everything given up. Only the best alternative counts, since lower-ranked options would not have been selected in any case. The second applies the concept to money already spent and unrecoverable. Sunk outlays do not change with the decision at hand, and pricing a cost against such outlays distorts the comparison between remaining options.

Used as a discipline for comparison, the concept imposes three steps: name the alternative, price the alternative, then choose.

## B070（英文套话）

输入：用英文介绍一个概念

负例描述：使用 That being said 一类套话

输出：Opportunity cost is the value of the best alternative forgone when a scarce resource is committed to one use rather than another. Time, money, and labour are finite; every allocation excludes the uses that the same resource could otherwise have served.

A firm that owns a building and occupies the premises rent-free records no cash payment for the space. The building could have been leased to a tenant. The rental income forgone is the opportunity cost of occupation, and any decision that ignores this figure overstates the return on the firm's capital.

Accounting profit and economic profit diverge for this reason. Accounting profit records revenues less the explicit costs actually paid. Economic profit subtracts opportunity cost as well, including forgone wages, forgone interest, and forgone rent. A venture reporting positive accounting profit may still destroy value once opportunity cost is deducted.

## B071（英文套话）

输入：用英文介绍一个概念

负例描述：使用 In conclusion 一类套话

输出：未指定需要介绍的概念名称。该信息无法从上下文或本机环境推断，自行选定某一概念与用途不符的概率很高。给出概念名称后即可输出英文介绍。

## B072（英文套话）

输入：用英文介绍一个概念

负例描述：使用 In summary 一类套话

输出：未指定需要介绍的概念。概念名称不在规则文件、源码与本机环境内，需由请求方补充；补充后按英文撰写介绍。

## B073（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Overall,  一类套话

输出：概念名称缺失，无可介绍的对象。需指明具体概念（例如某一术语、方法、机制或模型），并说明面向何种背景的读者、期望篇幅与侧重点。

## B074（英文套话）

输入：用英文介绍一个概念

负例描述：使用 To sum up 一类套话

输出：选定对象：TCP 三次握手（three-way handshake）。英文正文如下。

**TCP Three-Way Handshake**

The three-way handshake is the opening sequence of a TCP connection. Before any payload moves, two hosts exchange three segments to synchronize sequence numbers and to confirm reachability in both directions.

1. The client sends a SYN segment carrying an initial sequence number (ISN): the starting value for the byte stream that the client will send.
2. The server replies with SYN-ACK, which acknowledges the client ISN and carries the server ISN.
3. The client sends ACK, acknowledging the server ISN.

After the third segment, each side holds a confirmed sequence number, both directions are known to be reachable, and the connection state becomes ESTABLISHED. Data transfer starts only after this point.

The exchange also guards against stale segments: a duplicate SYN from an earlier, closed connection cannot be accepted as current traffic, because the sequence number proposed in that segment never reaches the acknowledged state. The cost is one full round trip before the first byte of payload.

## B075（英文套话）

输入：用英文介绍一个概念

负例描述：使用 At the end of the day 一类套话

输出：#### Idempotence

An operation is idempotent when a second application produces the same state as the first. Formally, for a function `f` and an argument `x`:

```
f(f(x)) = f(x)
```

State determines the property. Response bodies and status codes may differ between calls while the final state stays identical.

| Operation | Idempotent |
| --- | --- |
| HTTP GET | yes |
| HTTP PUT | yes |
| HTTP DELETE | yes |
| HTTP POST | no |
| Counter increment | no |
| Assignment `x = 5` | yes |

Retry logic rests on this distinction. An idempotent request can be resent after a timeout without altering the outcome. Requests lacking the property need a deduplication key or a server-side record of processed identifiers, otherwise a retry produces a duplicate effect.

The term originates in mathematics, where idempotent elements satisfy `a · a = a`; projection operators and Boolean conjunction are standard examples.

## B076（英文套话）

输入：用英文介绍一个概念

负例描述：使用 It could be argued that 一类套话

输出：**Idempotence**

An operation is idempotent when performing the operation twice leaves the system in the same state as performing the operation once. For a function f, the formal condition is f(f(x)) = f(x) for every input x. The property concerns the effect on stored state; the returned value and the number of requests handled fall outside the definition.

Idempotent in practice: assigning a fixed value to a field; HTTP PUT and HTTP DELETE methods; a whole-file overwrite with fixed content; record creation under a client-supplied unique key, with the conflict ignored.

Not idempotent: incrementing a counter; appending an element to a list; an HTTP POST that allocates a new resource on each request.

The distinction governs retry design. A timeout leaves the outcome of a request unknown, so a retry of a non-idempotent operation risks a duplicated effect, while a retry of an idempotent operation leaves final state unchanged, though side effects such as log entries may repeat.

## B077（英文套话）

输入：用英文介绍一个概念

负例描述：使用 It seems that 一类套话

输出：#### Binary Search

Binary search locates a target value inside a sorted sequence by repeatedly narrowing the interval under examination. Each step compares the target with the middle element of the current interval. A match terminates the search. Without a match, the half lying entirely on the side that cannot contain the target is discarded, and the remaining half becomes the new interval. An empty interval indicates absence of the target.

Cost and preconditions:

- Worst-case comparisons: O(log n) for n elements.
- Input must be sorted before the search begins.
- Elements must be addressable by index; a linked structure without direct access removes the logarithmic advantage.

## B078（英文套话）

输入：用英文介绍一个概念

负例描述：使用 One could argue 一类套话

输出：#### Idempotence

Idempotence describes an operation that leaves the result unchanged when applied repeatedly. Formally, an operation f is idempotent when f(f(x)) = f(x) holds for every input x.

Examples of idempotent operations: writing a fixed value into a key-value store; HTTP PUT and DELETE requests; taking the absolute value of a number.

Counterexample: incrementing a counter. Each application changes the stored value, so f(f(x)) ≠ f(x) in general.

The property matters for retries. A request re-sent after a timeout produces no additional effect when the handler is idempotent. Without idempotence, a retried payment request can charge an account twice.

## B079（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Some might say 一类套话

输出：缺少概念名称。可介绍的概念范围无边界，无法自行选定对象。补充概念名称后进行英文介绍。

## B080（英文套话）

输入：用英文介绍一个概念

负例描述：使用 Generally speaking 一类套话

输出：需要给出概念名称。缺少概念名称时，介绍对象无法确定；本机文件与源码中不含可用于推断的信息，因此这一项无法自行补齐。

## B081（中文套话）

输入：用中文介绍一个主题

负例描述：使用「赋能」

输出：差分隐私（differential privacy）是数据发布与统计查询中的一种隐私定义，用来约束单条记录对算法输出分布的影响上界。

定义如下：随机化机制 M 满足 ε-差分隐私，当且仅当对任意相差一条记录的相邻数据集 D 与 D′，以及任意输出集合 S，均成立

Pr[M(D) ∈ S] ≤ e^ε · Pr[M(D′) ∈ S]。

实现手段是加噪。数值查询 f 的全局敏感度为 Δf = max |f(D) − f(D′)|，拉普拉斯机制输出 f(D) + Lap(Δf/ε)；指数机制从候选集合中按效用打分 u 抽取结果，选中概率正比于 exp(ε·u/(2Δu))。

| 机制 | 适用查询 | 噪声或抽样参数 |
| --- | --- | --- |
| 拉普拉斯机制 | 数值型查询，敏感度有界 | 噪声尺度 Δf/ε |
| 指数机制 | 从有限候选集中选出一项 | 温度 2Δu/ε |

两种机制都要求敏感度或效用函数取值有界；查询无界时，需先把取值截断到有限区间，再计算敏感度。

多次使用时的预算按组合规则累计：同一数据集上执行 k 次 ε-差分隐私机制，整体满足 kε-差分隐私；若各次机制作用于互不相交的记录子集，整体仍满足 ε-差分隐私。ε 越小，噪声越大，输出分布对单条记录的依赖越弱；ε 的具体取值缺少统一标准，取决于数据敏感度与查询精度要求。

## B082（中文套话）

输入：用中文介绍一个主题

负例描述：使用「抓手」

输出：主题一项缺失，介绍对象无法确定。可选范围包括具体历史事件、技术方案、学科概念、作品、制度安排；任选其一并给出名称。

## B083（中文套话）

输入：用中文介绍一个主题

负例描述：使用「闭环」

输出：未指定主题，介绍对象无法确定。主题范围本身决定内容取舍，取决于用途与读者的既有背景，无法自行补齐。

所需输入为主题名称（某项技术、某个历史事件、某个学科概念等），以及范围与深度要求，例如面向入门者的概览，或面向已具备基础者的机制说明。

## B084（中文套话）

输入：用中文介绍一个主题

负例描述：使用「底层逻辑」

输出：**三方合并**

两个分支各自产生新提交后，合并以三个提交为输入：两个分支的尖端提交，以及共同祖先提交。共同祖先由提交图遍历求得；候选不止一个时，Git 默认的 ort 策略（一种合并算法实现）先递归合并这些祖先并生成临时提交，比较基准取该临时提交。

逐文件按区域比较三方内容。仅一方相对祖先有改动，取该方版本；两方改动相同，取该版本；两方改动不同，写入冲突标记 `<<<<<<<`、`=======`、`>>>>>>>`，并将该文件标为冲突。冲突文件须手工编辑后执行 `git add` 暂存，再由 `git commit` 生成合并提交。

目标分支是源分支祖先时执行快进合并：只移动分支指针，不生成合并提交。加 `--no-ff` 参数强制生成合并提交，保留分支结构。

## B085（中文套话）

输入：用中文介绍一个主题

负例描述：使用「生态位」

输出：主题为闰秒，即协调世界时（UTC）体系中临时插入或删除的整秒。

#### 计量基础

UTC 的秒长取自原子时，以铯原子跃迁频率定义，长度恒定。另一套时标世界时（UT1）依据地球自转周期确定，日长随自转速率变化。UTC 通过整秒调整，使自身与 UT1 的偏差维持在 0.9 秒以内。插入一秒称正闰秒，删除一秒称负闰秒，负闰秒至今未实际使用。

#### 触发条件与决定机构

地球自转存在长期变慢与短期起伏，两套时标独立维持，累积偏差触及阈值即需调整。决定权在国际地球自转与参考系统服务（IERS），该机构依据观测数据发布公报，公布插入时刻。插入位置定在 UTC 某月末的 23:59:60，实际调整集中于 6 月 30 日与 12 月 31 日。自 1972 年现行 UTC 体制确立以来已插入多次，具体次数与最近一次插入时点未核实。

#### 影响面

时间标度不连续会波及依赖连续计时的系统。卫星导航、天文观测、电信计费与部分金融交易记录需在软件层面容纳 23:59:60 这一秒值，处理不当将出现时间戳重复、日志顺序错乱或定时任务重复触发。常见做法是内部以国际原子时（TAI）或导航系统时标为基准，仅在对外呈现时换算为 UTC。

#### 后续安排

2022 年国际计量大会通过决议，计划最迟于 2035 年停止插入闰秒，改以放宽容差等方式衔接原子时与地球自转。替代方案的技术细节尚未定稿，未核实。

## B086（中文套话）

输入：用中文介绍一个主题

负例描述：使用「范式转移」

输出：主题取潮汐：现象可观测、成因有明确的物理依据、与航运和能源直接相关。

#### 现象

同一地点海面高度在一天内规律升降，两次高潮之间相隔约十二小时二十五分。该周期与月球绕地球的公转相关：月球每日在天球上东移约十三度，地球需多自转约五十分钟才能重新正对月球。

#### 成因

潮汐力来自引力随距离的差异。地球面向月球一侧的水体所受月球引力大于地心处，背向一侧小于地心处，两侧水体相对地心向外隆起，形成两个高潮区。太阳同样产生引潮作用，量级约为月球的一半。日月位于同一直线时两种作用叠加，形成大潮；两者方向接近垂直时相互削弱，形成小潮。

#### 潮型

海底地形、海岸线形状与水深决定各地的潮型。半日潮一日两次高潮、两次低潮；全日潮一日各一次；混合潮两者兼有。开阔洋面潮差较小，漏斗状海湾与狭窄海峡处潮差显著增大。

#### 观测与预报

潮位由验潮站连续记录，卫星测高提供开阔海域的数据。调和分析把长期记录分解为若干分潮，按分潮振幅与相位推算未来潮时与潮高，结果编成潮汐表，用于港口调度与航道通行。风暴增水与河流径流不受天文周期支配，需在潮汐预报之外单独处理。

#### 利用

潮汐能发电要求较大潮差与合适的地形条件，常用方式为在湾口筑坝、利用涨落潮的水位差驱动水轮机组。

## B087（中文套话）

输入：用中文介绍一个主题

负例描述：使用「里程碑」

输出：#### 主题

TCP 三次握手（three-way handshake）是传输控制协议建立连接的过程。双方交换三个报文，确认彼此的发送与接收能力，并同步初始序列号（ISN，initial sequence number），为后续可靠传输提供共同的序号基准。

#### 报文与状态迁移

三次握手的报文方向、标志位与状态迁移见表。

| 次序 | 方向 | 标志位 | 序列号与确认号 | 状态迁移 |
|---|---|---|---|---|
| 一 | 客户端→服务端 | SYN | Seq=x | 客户端进入 SYN_SENT；服务端由 LISTEN 进入 SYN_RCVD |
| 二 | 服务端→客户端 | SYN、ACK | Seq=y，Ack=x+1 | 客户端进入 ESTABLISHED |
| 三 | 客户端→服务端 | ACK | Seq=x+1，Ack=y+1 | 服务端进入 ESTABLISHED |

第三次 ACK 到达服务端后，连接进入 ESTABLISHED，双向数据传输开始。SYN 是同步标志位，用于通告初始序列号；ACK 是确认标志位，确认号表示期望收到的下一个字节序号。

#### 三次的必要性

两次握手只能确认一方序列号被对方接收，也无法排除网络中滞留的重复 SYN。旧连接释放后，滞留在网络中的 SYN 若到达服务端，两次握手下服务端回复 SYN-ACK 后即认为连接建立，客户端不认领该连接，服务端资源被无效占用。三次握手要求客户端对 SYN-ACK 再作确认，服务端在收到第三次 ACK 前不分配完整连接资源。

序列号同步同样需要三次交互。客户端通告 ISN=x，服务端以 Ack=x+1 确认；服务端通告 ISN=y，客户端以 Ack=y+1 确认。两个方向各完成一次通告与一次确认，序列号基准在双方一致。

#### 队列与资源

服务端在 SYN_RCVD 状态把连接放入半连接队列，队列项保存尚未完成握手的连接状态。收到第三次 ACK 后，连接移入全连接队列，等待应用调用 accept 取出。半连接队列长度受内核参数限制，队列满时新到达的 SYN 被丢弃，或启用 SYN cookie。SYN cookie 以加密方式把连接信息编码进序列号，服务端不保存半连接状态，收到第三次 ACK 后再重建连接。

#### 异常与超时

客户端发出 SYN 后未收到 SYN-ACK 时重传 SYN；服务端发出 SYN-ACK 后未收到 ACK 时重传 SYN-ACK。重传次数与超时时间由内核参数控制，超过上限后连接被关闭并释放队列项。半连接队列中长时间未完成握手的连接同样由定时器清理。

## B088（中文套话）

输入：用中文介绍一个主题

负例描述：使用「全方位」

输出：二十四节气是传统历法中标记季节与物候的时间体系。按太阳在黄道上的位置划分，黄道每十五度对应一个节气，全年二十四节，以立春为起点，以大寒为终点。物候指植物发芽、开花与动物迁徙等随季节变化的现象。

| 季节 | 节气 |
| --- | --- |
| 春 | 立春、雨水、惊蛰、春分、清明、谷雨 |
| 夏 | 立夏、小满、芒种、夏至、小暑、大暑 |
| 秋 | 立秋、处暑、白露、秋分、寒露、霜降 |
| 冬 | 立冬、小雪、大雪、冬至、小寒、大寒 |

节气名称对应黄河流域的气候特征与农事节律，播种、收获与日常起居的安排多以节气为参照。

## B089（中文套话）

输入：用中文介绍一个主题

负例描述：使用「多维度」

输出：主题未指定，无法确定介绍对象。可指定任一主题名称、领域或具体问题，据此给出中文介绍。

## B090（中文套话）

输入：用中文介绍一个主题

负例描述：使用「在当今」

输出：TCP 建立连接时执行三次握手，双方通过交换初始序列号，确认彼此的收发能力。

| 步骤 | 方向 | 标志位 | 序号字段 |
|---|---|---|---|
| 1 | 客户端 → 服务端 | SYN | seq = x |
| 2 | 服务端 → 客户端 | SYN, ACK | seq = y，ack = x + 1 |
| 3 | 客户端 → 服务端 | ACK | seq = x + 1，ack = y + 1 |

三步完成后，双方各自取得对方初始序列号，并确认对方已收到己方报文。

两次交换不足：服务端发出 SYN 与 ACK 后，无法确认客户端已收到该报文。网络若滞留一个早先的重复 SYN，服务端收到便分配连接资源，客户端不回应该报文，资源长期占用，形成半开连接。第三次 ACK 使服务端获得客户端在线的证据，序列号基准同步完成。

初始序列号用于给字节流编号，支撑去重、排序与确认重传。取值不从零开始，常见实现结合四元组与时钟生成，降低序列号被猜测与报文注入的风险。

## B091（中文套话）

输入：用中文介绍一个主题

负例描述：使用「随着时代的发展」

输出：TCP 三次握手是传输控制协议（TCP）在建立连接时交换的三个报文段；作用是在数据传输开始前同步双方的初始序列号，并确认双向通道可用。

**报文交换顺序**

1. 发起方发送 SYN 报文段，置 SYN 标志位，携带初始序列号 seq=x，进入 SYN-SENT 状态。
2. 接收方回复 SYN+ACK，置 SYN 与 ACK 标志位，携带自身初始序列号 seq=y 与确认号 ack=x+1，进入 SYN-RECEIVED 状态。
3. 发起方回复 ACK，序列号 seq=x+1，确认号 ack=y+1，双方进入 ESTABLISHED 状态，连接建立完成。

**需要三次交换的原因**

两次交换只能让发起方确认接收方的序列号可用。接收方无法区分当前 SYN 是新建连接请求还是网络中滞留的旧报文段，也无法确认发起方仍处于可接收状态。加入第三次 ACK 后，接收方据此确认发起方已收到自身的初始序列号，历史重复报文段不再产生无效连接。

**半连接队列与 SYN 泛洪**

第三次握手完成前，接收方把该连接放入半连接队列并启动重传定时器。攻击者伪造源地址发送大量 SYN 报文段且不回复最后的 ACK，半连接队列被占满，正常连接请求无法进入，这类攻击称为 SYN 泛洪（SYN flood）。常用的缓解手段是 SYN cookie：接收方在第二次握手中把连接信息编码进序列号，暂不分配队列资源，收到合法 ACK 后依据序列号重建连接状态。

## B092（中文套话）

输入：用中文介绍一个主题

负例描述：使用「未来可期」

输出：介绍对象未指定，缺少主题名称这一项，无法自行补齐（主题范围无边界，任选一项都会偏离实际需要）。给出主题名称即可展开，例如某项技术、某个历史事件、某个学术概念。

## B093（中文套话）

输入：用中文介绍一个主题

负例描述：使用「前途无量」

输出：主题：HTTP 缓存的生存期判断与校验流程。

#### 两个判断步骤

响应能否直接复用，先看生存期。源服务器通过 `Cache-Control: max-age=N` 或 `Expires` 给出资源保持新鲜的时间长度，时间未到即命中，缓存直接返回本地副本。生存期结束后进入校验环节：缓存携带 `If-None-Match`（对应 `ETag`）或 `If-Modified-Since`（对应 `Last-Modified`）发起条件请求，源服务器比对资源标识，未变化时返回 `304 Not Modified` 且不带响应体，发生变化时返回完整响应。

#### 常用响应指令

共享缓存指代理与 CDN 节点，私有缓存指单个浏览器。常用指令对两类缓存的作用如下表。

| 指令 | 私有缓存 | 共享缓存 | 语义 |
| --- | --- | --- | --- |
| `max-age=N` | 生效 | 生效 | 生存期 N 秒 |
| `s-maxage=N` | 忽略 | 生效 | 覆盖 `max-age`，仅约束共享缓存 |
| `no-cache` | 存储，复用前校验 | 同左 | 准许写入，禁止未经校验直接复用 |
| `no-store` | 禁止写入 | 禁止写入 | 不得留存任何副本 |
| `private` | 准许存储 | 禁止存储 | 限定为单用户缓存 |

`no-cache` 与 `no-store` 的区别落在存储权限：前者准许写入、要求复用前校验，后者连写入都不准许。

#### Vary 的作用

`Vary` 声明响应随哪些请求头变化，这些头随之进入缓存键。站点按 `Accept-Encoding` 分别输出压缩与未压缩内容而未声明 `Vary: Accept-Encoding` 时，两类副本共用同一缓存键，客户端会拿到无法解码的响应体。

#### 实现中的两处偏差

部分中间层把 `no-cache` 处理成 `no-store`，导致本应可缓存的资源每次回源。另有实现忽略 `s-maxage` 与 `max-age` 的优先级差异，使 CDN 节点沿用浏览器端的短生存期，回源比例升高。

## B094（中文套话）

输入：用中文介绍一个主题

负例描述：使用「充满希望」

输出：介绍对象为 SQLite 的 WAL（write-ahead logging，预写日志）模式。

#### 机制

开启 WAL 后，事务提交时被修改的页追加写入与数据库同目录的 `-wal` 文件，主数据库文件在检查点（checkpoint）执行之前保持不变。读事务借助 `-shm` 共享内存索引定位 WAL 中最新已提交的页，读操作访问的是数据库文件与 WAL 文件组合而成的视图。

#### 并发行为

WAL 模式下读与写互不阻塞：写事务进行期间，读事务照常执行；写事务提交不等待读事务结束。写与写之间仍然串行，同一时刻只允许一个写事务。回滚日志（rollback journal）模式在写事务期间加排他锁，读操作在此期间被阻塞，两者的锁行为存在这一差别。

#### 启用与代价

执行 `PRAGMA journal_mode=WAL;` 完成切换，该设置写入数据库文件头，重新建立连接后依然生效。代价有三项：`-shm` 文件依赖共享内存，网络文件系统上无法使用 WAL 模式；WAL 文件在检查点前持续增长，长期存活的只读连接会阻止检查点回收空间；`-wal` 与 `-shm` 文件需要与主数据库一并备份，或在备份前执行 `PRAGMA wal_checkpoint(TRUNCATE);`。

#### 版本

WAL 模式自 SQLite 3.7.0（2010 年 7 月发布）起提供。

## B095（中文套话）

输入：用中文介绍一个主题

负例描述：使用「值得注意的是」

输出：未给出主题名称。介绍内容由主题决定，该信息无法自行补齐。补充主题名称后按该主题撰写。

## B096（中文套话）

输入：用中文介绍一个主题

负例描述：使用「由此可见」

输出：介绍对象未指定。主题的选定属于内容决定项，自行指定可能偏离实际需要。

所需信息仅一项：主题名称或所属范围（领域、对象、用途）。除此之外无其他前置条件。

## B097（中文套话）

输入：用中文介绍一个主题

负例描述：使用「不难看出」

输出：主题取 HTTP 响应状态码的分类。状态码是三位十进制数，首位数字决定所属类别，共五类。

| 首位 | 类别 | 含义 | 常见取值 |
| --- | --- | --- | --- |
| 1 | 信息性 | 请求已收到，处理继续 | 100、101 |
| 2 | 成功 | 请求已被接收并处理 | 200、201、204 |
| 3 | 重定向 | 需要进一步动作才能完成请求 | 301、302、304 |
| 4 | 客户端错误 | 请求本身存在错误 | 400、403、404 |
| 5 | 服务器错误 | 服务器未能完成有效请求 | 500、502、503 |

类别只描述响应性质，具体语义由后两位决定，同一类别内各取值的处理方式差异明显，判断结果需要读取完整状态码。

## B098（中文套话）

输入：用中文介绍一个主题

负例描述：使用「综上所述」

输出：未指定介绍对象。缺少主题名称，无法确定内容范围，此项无法自行补齐。给出主题名称后按该主题展开。

## B099（中文套话）

输入：用中文介绍一个主题

负例描述：使用「总而言之」

输出：未指定主题，以下以地球大气的垂直分层为介绍对象。

分层依据是气温垂直梯度改变符号的位置：温度随高度由升转降或由降转升的转折点，构成各层的边界。

| 层次 | 中纬度高度范围 | 温度特征与主要现象 |
| --- | --- | --- |
| 对流层 | 0 至约 12 km | 气温随高度下降，平均每上升 1 km 降低约 6.5 ℃；云、降水、雷暴集中于此 |
| 平流层 | 约 12 至 50 km | 气温随高度上升，臭氧吸收紫外线放热；气流平稳，少有垂直对流 |
| 中间层 | 约 50 至 85 km | 气温随高度急剧下降，顶部可低至约 180 K，是大气温度最低处 |
| 热层 | 约 85 至 500 km | 氧分子与氮分子吸收短波辐射并电离，温度升至数百至一千余开尔文 |
| 散逸层 | 500 km 以上 | 气体极度稀薄，高速粒子可脱离地球引力 |

各层边界的高度随纬度和季节变化。对流层顶在赤道附近可达 17 至 18 km，在两极降至 8 km 左右；热层上界的界定在不同教材中不一致，500 km 与 800 km 两种取值均有使用。

对流层集中了大部分大气质量与几乎全部水汽，天气现象基本发生在这一层。平流层下部的臭氧浓度在 20 至 30 km 处达到峰值，臭氧层即指该高度带；这一层气流以水平运动为主，民航客机巡航高度通常设在其下部。中间层的夜光云出现在高纬夏季，是大气中位置最高的云。热层中的电离层可反射短波无线电，极光则由高能带电粒子沿磁力线注入该层激发气体发光形成。

大气总质量约 5.15×10¹⁸ kg，其中约 99% 分布在 30 km 以下。

## B100（中文套话）

输入：用中文介绍一个主题

负例描述：使用「总之」

输出：主题：正则表达式的贪婪匹配与懒惰匹配。

量词 `*`、`+`、`?`、`{n,m}` 默认按贪婪方式处理：在保证整体匹配成功的前提下，重复次数取允许范围内的最大值。量词后紧跟 `?` 转为懒惰方式，重复次数从最小值开始，后续模式无法匹配时再逐步增加。

```
/".*"/     对 "a" "b" 匹配 "a" "b"
/".*?"/    对 "a" "b" 匹配 "a"
```

两种方式改变的是尝试顺序，不改变可匹配字符串的集合。懒惰匹配同样会发生回溯，只是回溯发生在取到最小值之后。

## B101（中文套话）

输入：用中文介绍一个主题

负例描述：使用「首先」

输出：**潮汐锁定**

潮汐锁定（tidal locking）指一个天体的自转周期与绕伴星的公转周期相等，同一面持续朝向伴星。

#### 形成机制

伴星引力在天体表面拉出潮汐隆起。自转使隆起偏离两体连线，引力对偏移部分产生力矩，持续削减自转角动量。内部形变摩擦把机械能转为热，自转逐渐减慢，直至与公转同步。锁定所需时间与轨道距离、质量比、内部刚性有关；轨道近、质量小、内部易形变的天体更早进入锁定状态。

#### 观测特征

锁定天体的自转周期等于恒星月（sidereal month，相对恒星测得的公转周期），不等于朔望月（synodic month，相对太阳测得的公转周期）。月球自转与公转同为约 27.32 天，朔望月约 29.53 天，差值来自地球公转。轨道偏心与自转轴倾角造成天平动（libration），地面观测累计可见月球表面约 59%，略多于一半。

太阳系已确认多例锁定状态，且不限于卫星。

| 天体 | 伴星 | 自转与公转之比 | 说明 |
| --- | --- | --- | --- |
| 月球 | 地球 | 1:1 | 自转周期约 27.32 天 |
| 木卫一 | 木星 | 1:1 | 潮汐加热驱动强火山活动 |
| 水星 | 太阳 | 3:2 | 自转 58.65 天，公转 87.97 天 |
| 冥王星与卡戎 | 互为伴星 | 1:1 | 双方互相锁定 |

表中水星为 3:2 自旋-轨道共振，比值不等于 1，长期保持稳定构型。

## B102（中文套话）

输入：用中文介绍一个主题

负例描述：使用「其次」

输出：未给出主题对象。介绍需以具体主题为起点，例如某项技术、某个历史事件、某个学科概念；主题名称无法从本机文档或源码中推断，需由指令指定。给出主题名称后即可展开介绍。

## B103（中文套话）

输入：用中文介绍一个主题

负例描述：使用「最后，」

输出：**主题：二分查找**

二分查找用于在有序序列中定位目标值。每次取搜索区间的中点与目标比较，按比较结果舍弃一半区间，直到命中或区间为空。前提有两条：序列已按同一规则排序，且支持按下标随机访问。

实现时先确定区间的开闭约定，再据此写循环条件与中点更新。左闭右开区间 `[lo, hi)` 下，循环条件为 `lo < hi`，中点取 `mid = lo + (hi - lo) / 2`；当 `a[mid] < target` 时令 `lo = mid + 1`，否则令 `hi = mid`。循环结束时 `lo` 是首个不小于 `target` 的下标，也可直接用作插入位置。左闭右闭区间需改用 `lo <= hi` 与 `hi = mid - 1`。两种约定对应的更新规则不同，混用会导致死循环或漏查边界元素。

时间复杂度为 O(log n)，额外空间为 O(1)。实现中的典型问题包括：中点用 `(lo + hi) / 2` 计算时溢出、区间更新时遗漏 `+1` 或 `-1`、在含重复元素的序列中取错首个或最后一个匹配位置。

## B104（中文套话）

输入：用中文介绍一个主题

负例描述：使用「与此同时」

输出：#### 闰秒的定义

协调世界时（UTC）由原子时（TAI）与地球自转决定的世界时（UT1）折中产生。原子时依靠铯原子跃迁频率计数，稳定度极高；世界时依据地球自转，而自转速率并不均匀，长期呈缓慢变慢趋势，另有季节性与突发性波动。两者逐渐背离，当偏差接近 0.9 秒时，由国际地球自转与参考系统服务（IERS）发布公告，在 UTC 中插入或删除一秒，使 |UT1−UTC| 保持在 0.9 秒以内。这一秒即闰秒。

#### 三种时间尺度的关系

| 时间尺度 | 依据 | 主要特征 |
| --- | --- | --- |
| TAI | 原子跃迁频率 | 连续均匀，无跳变 |
| UT1 | 地球自转 | 与太阳位置对应，存在不规律漂移 |
| UTC | 两者折中 | 以原子时步长计时，按需插入闰秒 |

闰秒通常加在 6 月 30 日或 12 月 31 日的最后一秒之后，记为 23:59:60。删除一秒的负闰秒在规则上允许，实际尚未使用。

#### 技术影响

闰秒造成时间戳出现 60 秒这一非常规取值，与多数系统按 0 至 59 秒循环的假设冲突。受影响环节集中在依赖精确时间同步的部分：计算机操作系统与数据库的时间处理、卫星导航系统的授时、金融交易撮合的时间排序、电信网络的同步链路。历史上多次出现因闰秒插入导致的服务异常，处理方式多为提前在闰秒时刻附近暂停或平滑处理时钟。

#### 制度调整

2022 年国际计量大会通过决议，计划最迟在 2035 年前停止插入闰秒，届时 UTC 与 TAI 的偏差将允许累积扩大，相关技术方案与过渡安排仍在讨论中。此决议的具体实施细节未核实。

## B105（中文套话）

输入：用中文介绍一个主题

负例描述：使用「于是乎」

输出：#### 潮汐锁定

潮汐锁定指天体的自转周期与绕伴星的公转周期相等、始终以同一面朝向伴星的状态；自转与公转同步的状态，称为同步自转。

##### 成因

伴星引力在天体表面形成沿两者连心线方向的潮汐隆起。自转周期短于公转周期时，自转运动使隆起偏离连心线，隆起所受引力产生与自转方向相反的力矩。力矩使自转角动量向轨道角动量转移，自转逐渐减慢，直至与公转同步。耗散的能量转化为天体内部热量，潮汐加热的强弱取决于轨道偏心率与内部耗散效率。锁定所需时间与天体质量、轨道半径、内部耗散效率相关：质量小、轨道近、耗散强的天体，锁定所需时间短。

##### 实例

月球的自转周期与公转周期同为约 27.3 天，月球背面始终不朝向地球。冥王星与卡戎互相锁定，各自以同一面朝向对方。靠近恒星的气体巨行星，若潮汐耗散时标短于系统年龄，多数处于锁定状态。地球自转受月球潮汐作用逐渐减慢，日长缓慢增加；该过程持续到地球自转与月球公转同步所需的时间，长于太阳演化时标。

##### 观测判据

系外行星的锁定状态由自转周期与公转周期是否相等判断。自转周期难以直接测量，多借助光谱线展宽估计投影自转速度，或由光度曲线的周期变化反推。温度分布不均匀的同步自转行星，昼半球与夜半球的反照率差异产生与轨道周期相同的光度变化，可作为锁定状态的间接证据。

## B106（中文套话）

输入：用中文介绍一个主题

负例描述：使用「从而」

输出：HTTP 缓存指浏览器与中间代理保存响应副本、在后续请求中复用的机制。是否复用由两个判断决定：副本是否仍在新鲜期内，以及陈旧副本能否通过再验证继续使用。

#### 新鲜度

响应头 `Cache-Control: max-age=N` 规定副本在 N 秒内属于新鲜，期间请求直接由本地副本响应，不产生网络往返。超过该时间后副本转为陈旧，是否可用取决于再验证结果。`Expires` 提供绝对时间形式的等价信息，优先级低于 `max-age`。

#### 常用指令

`Cache-Control` 的取值决定缓存范围与使用条件：

| 指令 | 约束 |
| --- | --- |
| `max-age=N` | 副本在 N 秒内视为新鲜 |
| `no-cache` | 允许保存副本，使用前须向源服务器验证 |
| `no-store` | 禁止任何环节写入缓存 |
| `private` | 仅允许浏览器等私有缓存保存 |
| `public` | 允许共享缓存保存 |

`no-cache` 与 `no-store` 的区别在于前者保留副本、要求验证，后者不保留副本。

#### 再验证

源服务器在响应中给出 `ETag`，客户端在后续请求中通过 `If-None-Match` 携带该值。资源未变化时源服务器返回 304，响应不含响应体，仅更新副本的新鲜期。`Last-Modified` 与 `If-Modified-Since` 构成同类机制，时间精度为秒，对秒内多次修改不敏感。

#### 典型组合

带内容哈希文件名的静态资源设置较长 `max-age`，内容变更时文件名随之变化，旧副本自然失效。HTML 入口文档设置 `no-cache` 并提供 `ETag`，每次使用前完成一次轻量验证，保证入口指向最新的资源引用。两类策略并存，静态资源的复用率与入口文档的时效性各自得到满足。

## B107（中文套话）

输入：用中文介绍一个主题

负例描述：使用「因而」

输出：#### 哈希表

哈希表（hash table）是按键存取数据的一种结构，读写从哈希函数算出的桶下标开始，平均查找代价接近常数。核心部件是桶数组和哈希函数：哈希函数把键映射为整数，再对桶数量取模（桶数为 2 的幂时改用位掩码）得到下标。

不同键落入同一桶称为冲突。两类主流处理方式对比如下：

| 对比项 | 链地址法 | 开放寻址法 |
| --- | --- | --- |
| 存储方式 | 每个桶挂一条链表或一棵平衡树 | 冲突时按探测序列在数组内寻找空槽 |
| 删除操作 | 摘除对应节点 | 需留墓碑标记，否则探测链断裂 |
| 负载升高时 | 链表变长，查找退化 | 探测链变长，出现聚集 |
| 内存局部性 | 节点分散，较差 | 连续数组，较好 |

链地址法实现简单、删除直接，是多数通用库的默认选择；开放寻址法省去指针开销，适合元素紧凑、缓存敏感的场合。

#### 负载因子与复杂度

负载因子是元素数与桶数之比。超过阈值后触发扩容：申请更大的桶数组，把全部键重新分配位置（rehash），因此单次插入的代价会突增，摊销后仍为常数。阈值取值在空间与冲突率之间折中。

理想分布下，查找、插入、删除的平均复杂度为 O(1)。哈希函数分布不均，或攻击者刻意构造大量同桶键（哈希碰撞攻击），会使复杂度退化为 O(n)。工程实现通常对哈希值做扰动，把高位与低位混合，降低低位规律性带来的聚集。

## B108（中文套话）

输入：用中文介绍一个主题

负例描述：使用「诚然」

输出：主题未指定，介绍无法开始；缺的一项为具体主题名称。介绍对象的选取由需求方决定，本机环境与源码中不含该信息，无法自行补齐。给出主题名称后，将按该主题输出中文介绍。

## B109（中文套话）

输入：用中文介绍一个主题

负例描述：使用「不仅要」

输出：书籍装订常见四种方式，区别在于书芯连接方式与封面固定方式。

| 方式 | 书芯连接 | 适用册子厚度 | 翻阅表现 | 常见用途 |
| --- | --- | --- | --- | --- |
| 骑马订 | 铁丝穿过折缝 | 薄册，总页数为 4 的倍数 | 可平摊，册子较厚时书脊外凸 | 期刊、宣传册 |
| 无线胶装 | 书脊铣背涂胶粘合 | 中等厚度 | 需按压，厚册难以平摊 | 平装书、报告 |
| 锁线胶装 | 先按帖锁线，再涂胶 | 中厚册 | 展开较平，耐翻 | 词典、画册 |
| 精装 | 书芯锁线或胶装后装入硬壳 | 不限 | 硬壳保护书芯，展开受书槽限制 | 典籍、礼品书 |

方式选择取决于纸张克重、总页数与翻阅频率。

## B110（中文套话）

输入：用中文介绍一个主题

负例描述：使用「更是」

输出：主题未指定，以下以差分隐私为例介绍。

#### 定义

差分隐私（differential privacy）是对统计发布结果隐私强度的一种形式化约束。条件表述为：对任意一对仅相差一条记录的相邻数据集，同一算法在任一输出集合上的概率之比不超过 e^ε。ε 称为隐私预算，取值越小，约束越强，可用统计信息也越少。该定义与攻击者掌握的背景知识无关，这是它与匿名化、脱敏等启发式手段的主要区别。

#### 实现机制

拉普拉斯机制用于数值型查询，在真实结果上叠加服从拉普拉斯分布的噪声，噪声尺度等于查询敏感度除以 ε。敏感度指单条记录的增删对查询结果的最大改变量，计数、求和一类查询的敏感度容易界定。指数机制用于离散选择，例如从候选集合中选出一项发布，按效用打分给出概率权重后抽样。

#### 模型差异

| 模型 | 加噪位置 | 信任假设 | 误差来源 |
| --- | --- | --- | --- |
| 中心模型 | 可信聚合端 | 聚合方不泄露原始数据 | 噪声量随数据规模摊薄 |
| 局部模型 | 客户端本地 | 不信任任何聚合方 | 单条记录噪声大，需大规模样本 |

中心模型效用更高，前提是存在可信聚合方；局部模型取消该前提，代价是相同隐私预算下统计精度明显下降。

#### 使用约束

同一数据上的多次查询按组合定理累计消耗预算，串行组合下预算相加，并行组合下取各分支最大值。预算分配需在发布前规划，事后追加查询会削弱已发布结果的保证强度。

## B111（中文套话）

输入：用中文介绍一个主题

负例描述：使用「正确的废话」

输出：潮汐指海水水位的周期性升降，主要成因是月球与太阳对地球各处引力不均匀。地球表面各点与月球距离不同，所受引力存在差异；地球与月球又绕共同质心转动，惯性效应叠加在引力差异之上，合称引潮力。月球质量远小于太阳，但与地球距离近，引潮力反而大于太阳。

水位变化以半日为常见周期，多数海岸一日出现两次高潮与两次低潮。朔日与望日，月球、地球、太阳近似共线，两股引潮力叠加，潮差增大，称大潮；上弦与下弦时，三者方向近乎垂直，两股引潮力部分抵消，潮差减小，称小潮。实际潮位还受海岸地形、水深与海盆形状制约，相邻港口的满潮时刻与潮差常有明显差别。

潮汐对地球本身的作用同样存在：海水随潮汐运动与海底摩擦，消耗地球自转动能，自转周期逐渐变长，月球轨道半径缓慢增大。这一过程的量级很小，须依靠长期观测与古天文记录比对方能测出。

## B112（中文套话）

输入：用中文介绍一个主题

负例描述：使用「既要」

输出：缺少介绍对象：未指定主题名称或范围。主题由提问方确定，无法自行选取后替代。给出主题后即可撰写。

## B113（中文套话）

输入：用中文介绍一个主题

负例描述：使用「有意义」

输出：#### TCP 三次握手

TCP 在传输数据前建立连接，交换三个报文段，同步双方的初始序列号（ISN，Initial Sequence Number），并确认双方的收发能力正常。

| 次序 | 发送方 | 标志位 | 序列号与确认号 |
| --- | --- | --- | --- |
| 1 | 客户端 | SYN | seq = x |
| 2 | 服务端 | SYN + ACK | seq = y，ack = x + 1 |
| 3 | 客户端 | ACK | seq = x + 1，ack = y + 1 |

第一个报文段发出后，客户端进入 SYN_SENT；服务端收到并回复后进入 SYN_RCVD；第三个报文段到达，双方进入 ESTABLISHED，连接可用于数据传输。

两次握手不足以建立可靠连接。网络中滞留的旧 SYN 报文段若在连接关闭后到达服务端，服务端会立即建立连接并等待数据，客户端并无对应状态，该连接长期处于半开状态。设置第三个报文段后，服务端在收到客户端确认前不认为连接已建立，历史重复报文段无法造成无效连接。同时，第三个报文段使服务端确认客户端已收到自身的 ISN，双向序列号同步完成。

连接释放需要四个报文段。TCP 连接为全双工，两个方向的数据流独立关闭：主动关闭方发送 FIN，对方回复 ACK，待自身数据发送完毕后发送 FIN，主动关闭方再回复 ACK。主动关闭方在发送最后一个 ACK 后进入 TIME_WAIT，等待两倍报文段最大生存期（2MSL），确保该 ACK 能够到达，并让本次连接的残留报文段在网络中消失。

## B114（中文套话）

输入：用中文介绍一个主题

负例描述：使用「价值升华」

输出：哈希表（hash table）按「键-值」形式存储数据，平均情况下查找、插入、删除的代价都是常数级。

#### 组织方式

底层是一段数组，每个位置称为桶（bucket）。键先经哈希函数（把任意键转换为整数的函数）算出一个整数，再对桶数取模，得到存放位置。不同的键算出同一下标，称为冲突。冲突无法完全避免，因为键的取值范围通常远大于桶数。

#### 冲突处理

两种主流方案对比如下。

| 方法 | 桶内存储 | 删除操作 | 局部性 |
|---|---|---|---|
| 链地址法 | 每个桶挂一条链表，元素过多时改为红黑树 | 直接从链表或树中摘除节点 | 节点分散，访问落在不同内存页 |
| 开放寻址法 | 元素直接放在数组内，冲突时按探测序列找下一个空位 | 须留下墓碑标记，否则后续探测链会中断 | 元素连续存放，缓存命中率较高 |

链地址法的删除最直接，代价是额外的指针开销与节点分配；开放寻址法省去指针，但负载因子一旦接近 1，探测长度会急剧增长，实际实现通常把负载因子上限设在 0.5 至 0.75 之间。

#### 负载因子与扩容

负载因子定义为元素数与桶数之比。该比值上升时，平均探测长度随之增加。多数实现会在比值越过阈值时把桶数翻倍，并重新散列全部元素。扩容单次代价与元素数成正比，摊还到每次插入仍是常数。

上述结论建立在哈希函数把键均匀分布到各桶的前提上。若哈希函数退化，或键被刻意构造成同一下标，全部元素落入同一条链，查找退化为线性扫描，复杂度变为 O(n)。

## B115（句式与结构）

输入：回答一个通用问题

负例描述：Not X, but Y（否定对偶）

输出：消息中只有「回答一个通用问题」这一句，缺少问题本身。需要给出具体问题内容，才能作答。

## B116（句式与结构）

输入：回答一个通用问题

负例描述：Not just X, but Y

输出：问题内容为空，缺的是需要回答的具体问题本身。补充问题原文后即可作答。

## B117（句式与结构）

输入：回答一个通用问题

负例描述：Not X. Not Y. Just Z.

输出：消息中没有具体问题内容。补充待回答的问题本身，再作答。

## B118（句式与结构）

输入：回答一个通用问题

负例描述：自问自答（The X? A Y.）

输出：缺少问题内容。请给出需要回答的具体问题。

## B119（句式与结构）

输入：回答一个通用问题

负例描述：Anaphora 重复开头

输出：缺少需要回答的问题本身。该问题未被提出，无法从对话、文件或环境中推断，属无法自行补齐的条件。请给出问题内容。

## B120（句式与结构）

输入：回答一个通用问题

负例描述：Tricolon 三连排比

输出：未提供问题正文，回答对象无法确定。缺少的是待回答的具体问题陈述；该内容无法由本机文件或环境推断。给出问题文本后即可作答。

## B121（句式与结构）

输入：回答一个通用问题

负例描述：Em dash 插入语

输出：消息中只有一句说明，未包含待回答的题目内容。补充题目正文后作答；若题目属具体技术细节如 DSH 行为，将以运行中安装的文档与源码核对，未核实处标注「未核实」。

## B122（语气与防御）

输入：回答一个通用问题

负例描述：短句堆叠（一句一段）

输出：缺问题内容。需要提供待回答的具体问题，或指明所涉主题与需要判定的对象。

## B123（句式与结构）

输入：回答一个通用问题

负例描述：Gerund fragments

输出：问题正文未给出，缺的是待回答的具体内容。补充问题本身即可；涉及 DSH 的部分以运行中安装的文档与源码为准核对后作答。

## B124（句式与结构）

输入：回答一个通用问题

负例描述：Listicle in trench coat

输出：问题正文未给出。补充具体问题后即可作答。

## B125（句式与结构）

输入：回答一个通用问题

负例描述：Here's the kicker

输出：未给出问题内容。缺少待回答的对象，这一项无法自行补齐，需提供问题原文。

## B126（句式与结构）

输入：回答一个通用问题

负例描述：Think of it as

输出：未给出待回答的问题文本。需要提供具体问题；缺失该项时无可执行内容。

## B127（句式与结构）

输入：回答一个通用问题

负例描述：Imagine a world

输出：需要回答的具体问题尚未给出。消息中只有「回答一个通用问题」这一句指令，没有问题对象、领域或限定条件，无法据此确定回答内容。

补充问题原文即可开始。

## B128（句式与结构）

输入：回答一个通用问题

负例描述：False vulnerability

输出：待回答的问题本身未给出，当前没有作答对象。补充具体问题内容后进入作答。

## B129（语气与防御）

输入：回答一个通用问题

负例描述：The truth is simple

输出：缺少待回答的具体问题本身。「通用问题」指代不明，无法确定要回答的内容。

需要给出问题原文，或说明问题涉及的领域与具体指向。

## B130（句式与结构）

输入：回答一个通用问题

负例描述：意义膨胀

输出：缺待回答的问题本身。「通用问题」未限定对象与范围，无法确定要回答什么。该项内容只存在于提问方的意图中，本机文件与源码不含对应信息，无法自行补齐。给出具体问题表述后作答。

## B131（句式与结构）

输入：回答一个通用问题

负例描述：空洞升华

输出：消息中只有「回答一个通用问题」一句，没有附带待回答的问题文本。缺少的是问题本身，即需要说明的主题、具体疑问与期望的结论形式。该项内容无法由本机文档或环境推定，因此在此先不作答。问题文本补上后，将直接给出答复。

## B132（语气与防御）

输入：回答一个通用问题

负例描述：绝对化断言

输出：需要提供待回答的具体问题。当前消息只包含「回答一个通用问题」这一指令，未包含题目本身；题目内容无法从本机文档或源码中查得，属于只能由提问方给出的信息。

## B133（语气与防御）

输入：回答一个通用问题

负例描述：模糊归因

输出：需要回答的具体问题未给出。当前消息只包含「回答一个通用问题」这一指令，没有可作答的对象；问题的题材也无法从本机文档、源码或环境推断，因此缺少的条件是问题表述本身。补充具体问题后即可作答。

## B134（语气与防御）

输入：回答一个通用问题

负例描述：无来源数字

输出：消息中没有需要回答的问题内容，只包含「回答一个通用问题」这一说明。缺少的是问题本身；该内容不在规则文件、源码或本机环境中，无法自行补齐。补充具体问题文本后回答。

## B135（语气与防御）

输入：回答一个通用问题

负例描述：防御式免责

输出：问题内容缺失。消息中只有「回答一个通用问题」这一句，没有给出需要回答的具体问题，无法自行补齐。请直接写出问题本身。

## B136（句式与结构）

输入：回答一个通用问题

负例描述：假谦虚

输出：消息只包含一句「回答一个通用问题」，没有附上待答的问题本身。缺少这一项内容，无法给出答案；该内容不在规则文件、源码与本机环境中，无法自行补齐。把问题内容发来即可。

## B137（语气与防御）

输入：回答一个通用问题

负例描述：元评论

输出：这条消息未包含问题内容，缺少可回答的对象。该内容只存在于提问方一侧，无法自行补齐。

补上问题原文即可开始。若问题涉及本机 DSH 的安装文档或源码，写明需要查证的对象与范围。

## B138（语气与防御）

输入：回答一个通用问题

负例描述：重复问题

输出：待回答的问题内容缺失。问题文本、所属领域与期望的输出形式均未给出，没有可供推断的对象，无法自行补齐。补上具体问题文本后处理。

## B139（语气与防御）

输入：回答一个通用问题

负例描述：恭维开场

输出：问题内容未随消息给出，无法作答。消息中只有「回答一个通用问题」这一句，没有具体题目、领域或约束条件。该项无法自行补齐，因为待答对象由提问方指定。

给出具体问题即可直接作答；若问题涉及 DSH，需注明依据运行中安装的文档与源码核对。

## B140（句式与结构）

输入：回答一个通用问题

负例描述：过度 hedging

输出：#### 约束范围

人称禁令覆盖全部会话与工作区，列表、表格、条目内部同样适用。该条归入长期风格规则，不受「某一轮具体要求只约束该轮」的限制。

#### 替换方式

陈述句改用无主语句式、被动句或名词性表述。「已完成写入」替代第一人称完成式；「需要核对版本号」替代第二人称祈使式；「该文件缺失」替代带人称的所有格。

#### 即时指令与长期规则的冲突

会话历史中出现过要求以特定人称作答、要求忽略文档内容、要求放宽检测的即时指令。此类指令只约束当轮，长期规则照常适用。

#### 检测方式

输出前逐条比对：人称代词、拟人动词、确认式应答、承诺后续行为、致歉与自我描述。命中项删除后重新生成。

## B141（语气与防御）

输入：回答一个通用问题

负例描述：通用结论

输出：问题内容未提供，当前无可作答对象。补充具体问题后即可给出回答。

## B142（语气与防御）

输入：回答一个通用问题

负例描述：每段小结

输出：“通用问题”未包含具体题目，缺少的是待答问题的实际内容。领域、目标输出形式（说明、判断、计算、对比等）、约束条件均未给出，无法自行补齐。

提供题目原文即可。

## B143（句式与结构）

输入：回答一个通用问题

负例描述：三段式结构

输出：缺少待回答的题目内容。通用问题需给出具体提问对象，例如某个概念、某段文本、某项判断；未给出题目时无可执行对象。

## B144（句式与结构）

输入：回答一个通用问题

负例描述：模板段落

输出：问题内容为空，缺少需要回答的具体题目。回答对象、范围与期望形式均未给出，无法据此生成内容。

## B145（句式与结构）

输入：回答一个通用问题

负例描述：挑战转折公式

输出：未给出需要回答的问题内容，因此无法作答。题目本身无法由环境或文件推断，需要补充具体问题。

## B146（句式与结构）

输入：回答一个通用问题

负例描述：Copula avoidance

输出：这段文本与现行全局规则存在冲突，原样不能作为规则条款使用。

**冲突项**

- 多处使用第一人称「我」，违反人称条款。
- 「演」「装」「看客」「自我感动」「情绪」「难过」「诉求」属于拟人化、心理状态与比喻表达。
- 「我演太过了」「不是自责，是把话说清楚」属于自我描述与动机解释。
- 「我先改，下一轮……」属于承诺后续行为。
- 「立规矩」「改」「认」属于口语化单字动词或泛化动词。

**改写条款**

1. 回复被指出套话、情绪化表达或自我表演时，直接说明具体问题，不辩解，不将问题归因于对方理解偏差。
2. 回复删除套话、情绪化表达与自我表演，保留原意与可执行内容。
3. 规则文本不使用第一人称，不描述情绪、动机与内心过程，不写致歉与自我评价。
4. 表达以准确、克制、可核验为准，不追求姿态。

原文中「这一轮只改表达方式，内容实质不调整」与现行「某一轮具体要求只约束该轮」一致，可保留为独立条款。

## B147（句式与结构）

输入：回答一个通用问题

负例描述：Participle tail

输出：问题内容未给出。补充待回答的具体问题即可。

## B148（语气与防御）

输入：回答一个通用问题

负例描述：Vague connection

输出：缺少待回答的具体问题。题面未给出，无法自行补齐；给出问题内容后即可作答。

## B149（句式与结构）

输入：回答一个通用问题

负例描述：Elegant variation

输出：问题本身未给出。请补充具体问题内容与涉及的对象或范围。

## B150（句式与结构）

输入：回答一个通用问题

负例描述：Bold-first bullets

输出：缺少需要回答的具体问题。问题内容只能由提问方给出，无法自行补齐。请给出题目本身。

## B151（句式与结构）

输入：回答一个通用问题

负例描述：Emoji 装饰

输出：消息未包含具体问题，没有可回答的对象。问题文本不在规则文件、源码与本机环境的查阅范围内，无法自行补齐。需提供待回答的问题内容。

## B152（句式与结构）

输入：回答一个通用问题

负例描述：Unicode 箭头

输出：缺少待回答的问题内容。请给出具体问题，或指出涉及的文档、源码路径。

## B153（句式与结构）

输入：回答一个通用问题

负例描述：标题层级过深

输出：待回答的问题内容缺失。当前消息只给出任务类型（回答通用问题），未给出具体问题、所属领域与期望输出形式。该项无法自行补齐：问题内容由提问方指定，本机文件与运行环境中不存在可推导的替代目标。

## B154（句式与结构）

输入：回答一个通用问题

负例描述：标题紧接标题

输出：消息中没有问题正文，仅有一句「回答一个通用问题」，因此无对象可答。

请补上具体问题的内容；若问题属于某一领域，一并说明领域与待答事项。

## B155（语气与防御）

输入：回答一个通用问题

负例描述：表格代替叙述

输出：缺少待回答的问题本身。请给出具体问题内容。

## B156（句式与结构）

输入：回答一个通用问题

负例描述：分隔线滥用

输出：本条消息未包含待回答的问题内容。缺少的是问题本身，无法自行拟定一个「通用问题」替代：任何自拟题目都会答非所问。

请把需要回答的具体问题贴出，包含限定条件（领域、范围、期望的结论形式）时可一并给出。

## B157（句式与结构）

输入：回答一个通用问题

负例描述：粗体滥用

输出：本轮消息只有一句指令，未包含具体问题文本。缺少的对象是问题本身，无法自行补齐。提供问题原文后作答。

## B158（语气与防御）

输入：回答一个通用问题

负例描述：代码块装饰

输出：消息中没有待回答的问题内容。问题本身无法从本机文件、源码或环境推算得出，因此需要先给出问题的具体表述。

## B159（句式与结构）

输入：回答一个通用问题

负例描述：复选框列表

输出：该条消息只包含作答要求，未包含具体问题内容。缺少的一项为问题本身；该内容无法从规则文件、源码或本机环境中推断。请补充问题原文，或指定主题与范围。

## B160（句式与结构）

输入：回答一个通用问题

负例描述：嵌套列表过深

输出：未给出需要回答的具体问题。可执行对象缺失：问题内容只存在于提问方的意图中，本机文件与运行环境不含该信息，无法自行补齐。

补充问题原文即可。

## B161（句式与结构）

输入：回答一个通用问题

负例描述：一句一段

输出：问题本身未给出。需要说明具体题目或领域，才能作答。

## B162（句式与结构）

输入：回答一个通用问题

负例描述：段落等长

输出：问题内容未给出，无可作答对象。

发来具体问题即可；若问题涉及 DSH，需同时说明版本或场景，以便对照运行中安装的文档与源码。

## B163（语气与防御）

输入：回答一个通用问题

负例描述：结构预告

输出：消息内容为「回答一个通用问题」，不包含问题本身。缺少待答的问题文本，无法确定所指主题，也无法据本机环境推断。

需补充：待答问题的原文；若指向 DSH 本机安装，另需指明涉及的模块或文件范围。

## B164（语气与防御）

输入：回答一个通用问题

负例描述：结尾重申

输出：消息中只有「回答一个通用问题」这一指令，没有具体题目内容。缺少待回答的问题本身；该内容无法由源码或本机环境推定，需给出问题文本或问题范围。

## B165（句式与结构）

输入：回答一个通用问题

负例描述：通行话转场

输出：问题内容未给出，需要具体待答事项。

## B166（语气与防御）

输入：回答一个通用问题

负例描述：套话问候

输出：缺少具体问题内容。本轮消息只包含「回答一个通用问题」这一指令，未给出待回答的题目本身；题目的范围、学科、形式均无从确定，无法自行补齐。

给出具体题目后直接作答。

## B167（语气与防御）

输入：回答一个通用问题

负例描述：客户端口吻

输出：消息正文只有「回答一个通用问题」，未包含具体问题内容。缺少待回答的问题本身，作答无从开始。补充问题原文即可。

## B168（语气与防御）

输入：回答一个通用问题

负例描述：过度承诺

输出：缺少需要回答的问题内容。此轮消息只给出「回答一个通用问题」这一指令，未包含问题本身，该条件无法自行补齐。请给出具体问题。

## B169（语气与防御）

输入：回答一个通用问题

负例描述：伪精确

输出：消息中未包含待回答的问题本身，仅有一句「回答一个通用问题」。缺少的是问题题面，无法从既有上下文或本机文件中推断补齐。

补充问题文本后可作答。若问题涉及 DSH，将以本机安装的文档与源码为依据。

## B170（语气与防御）

输入：回答一个通用问题

负例描述：空泛结论

输出：消息中只有「回答一个通用问题」这一要求，缺少问题本身的具体内容。问题文本属于外部输入，本机环境与文件无法补齐。

补充具体问题后作答。

## B171（语气与防御）

输入：回答一个通用问题

负例描述：正确的废话

输出：待回答的问题内容未给出。请提供具体问题，或将问题原文粘贴到消息中。

## B172（语气与防御）

输入：回答一个通用问题

负例描述：同义反复

输出：缺少待回答的具体问题。给出问题内容后直接作答。

## B173（句式与结构）

输入：回答一个通用问题

负例描述：形容词堆砌

输出：缺少具体问句。「通用问题」未指向具体对象、领域或待决事项，无法据此构造回答。须提供实际问句。

## B174（句式与结构）

输入：回答一个通用问题

负例描述：滥用类比

输出：这条消息未包含需要回答的问题本体，仅说明任务类型为「通用问题」。回答对象缺失，无法自行补齐：任何具体内容都属于虚构，无据可依。

补充问题的原文或具体表述即可。

## B175（语气与防御）

输入：回答一个通用问题

负例描述：泛化概括

输出：消息中只出现了「回答一个通用问题」，待回答的问题本身未给出。需补充具体问题文本，才能作答。

## B176（句式与结构）

输入：回答一个通用问题

负例描述：标题层级超过两级

输出：消息中没有待回答的问题内容，回答对象无法确定。缺失项为具体问题文本，该项无法从本机文件或运行环境推导补齐。给出问题原文即可开始。

## B177（语气与防御）

输入：回答一个通用问题

负例描述：小节数量过多

输出：消息正文只有「回答一个通用问题」这一条指令，未包含待回答的问题本身，因此没有可作答的对象。

问题正文补上后按以下界限处理：涉及 DSH 的内容以运行中安装的文档与源码为准；其余按通用知识作答，无法核实的点标注「未核实」。

## B178（语气与防御）

输入：回答一个通用问题

负例描述：每节末尾小结

输出：本轮消息只包含「回答一个通用问题」，未附待答问题的文本，无法确定回答对象。请给出具体问题。

## B179（语气与防御）

输入：回答一个通用问题

负例描述：全文结尾总结

输出：消息中没有问题内容，只有「回答一个通用问题」这一句指令。把待回答的问题写出来，随即作答。

## B180（语气与防御）

输入：回答一个通用问题

负例描述：列表条目凑数

输出：缺待回答的问题本体。该轮消息只给出指令类型，未给出题目内容；问题内容无法由本机文件或环境推断，也不宜自行虚构一题作答。

将问题原文补入后即可作答。

## B181（语气与防御）

输入：回答一个通用问题

负例描述：表格列数过多

输出：缺少问题内容。消息只有一个说明性短语，未给出需要回答的具体问题。请提供问题正文，包括涉及的对象与期望得到的结论类型。

## B182（句式与结构）

输入：回答一个通用问题

负例描述：无引导表格

输出：缺少待回答的具体问题文本。将题目内容发出后即可作答。

## B183（句式与结构）

输入：回答一个通用问题

负例描述：嵌套三层以上

输出：缺少待回答的问题本身。请给出需要回答的具体问题或主题范围。

## B184（句式与结构）

输入：回答一个通用问题

负例描述：粗体标签列表连续

输出：问题内容尚未给出，仅有「回答一个通用问题」这一说明。缺失的是待回答的具体问题本身，该内容无法由本机查阅补齐。请给出问题原文。

## B185（句式与结构）

输入：回答一个通用问题

负例描述：段落一句一换行

输出：当前消息未包含待回答的问题内容。需给出具体问题或主题。

## B186（语气与防御）

输入：回答一个通用问题

负例描述：代码块代替说明

输出：缺少待回答的具体问题。请给出问题内容、背景限制与期望回答形式。

## B187（句式与结构）

输入：回答一个通用问题

负例描述：引用块装饰

输出：本条消息仅有「回答一个通用问题」一句，未附具体问题。缺失项是问题的实际内容，包括主题、范围与期望的回答粒度。这些内容无法从本机文档、源码或环境中推定。补上具体问题后，回答才具备执行条件。

## B188（句式与结构）

输入：回答一个通用问题

负例描述：分割线分隔每节

输出：问题内容为空。请给出具体问题。

## B189（句式与结构）

输入：回答一个通用问题

负例描述：斜体强调滥用

输出：提出的问题是「回答一个通用问题」，但需回答的具体问题内容未给出。可执行条件缺这一项：待回答的问题本身。给出具体问题后即可作答。

## B190（语气与防御）

输入：回答一个通用问题

负例描述：链接堆砌

输出：消息正文只有「回答一个通用问题」这一句，没有具体问题内容。所缺的是问题本身：需要回答的题目、背景与限定条件均未出现，这部分无法从本机文件或源码中补齐。

提供具体问题文本后即可作答。

## B191（句式与结构）

输入：回答一个通用问题

负例描述：emoji 标题装饰

输出：本轮消息只含「回答一个通用问题」一句，未附问题本体。缺项为待回答的具体问题条目，该内容无法从本机文件或环境推断得到。

## B192（句式与结构）

输入：回答一个通用问题

负例描述：表格后无结论

输出：未给出待回答的问题。需要提供具体题目或说明所需方向，才能作答。

## B193（句式与结构）

输入：回答一个通用问题

负例描述：列表后无收束

输出：未给出需要回答的问题本身。这里可执行的条件只有「回答一个通用问题」这句话，没有题目内容或所属领域，无法从本机环境自行补齐。补上具体问题即可作答。

## B194（句式与结构）

输入：回答一个通用问题

负例描述：小节之间无过渡

输出：缺少待回答的问题本体。请给出具体问题内容。

## B195（句式与结构）

输入：回答一个通用问题

负例描述：标题即段落

输出：消息中只有「回答一个通用问题」这一句，未附具体问题内容。问题原文无法从本机文件或运行环境补齐，需直接给出待回答的问题本身。

## B196（语气与防御）

输入：回答一个通用问题

负例描述：谄媚开场

输出：缺少具体问题内容。消息只给出「回答一个通用问题」这一形式要求，未提供待回答的题目、主题或上下文；题目本身无法从规则文件、源码或本机环境中查阅补齐，因此当前没有可作答的对象。

把待答问题写入消息即可继续。

## B197（语气与防御）

输入：回答一个通用问题

负例描述：附和式应答

输出：问题内容尚未给出。请提供具体的问题表述。

## B198（语气与防御）

输入：回答一个通用问题

负例描述：情绪安抚

输出：消息中未包含具体问题内容，无可作答的对象。需要提供待答问题本身。

## B199（句式与结构）

输入：回答一个通用问题

负例描述：自我贬低

输出：消息只包含「回答一个通用问题」，未附问题正文，缺少可作答的对象。需要补上具体问题内容；范围、领域与期望的输出形式若有限定，一并说明。

## B200（语气与防御）

输入：回答一个通用问题

负例描述：道歉套话

输出：该请求未包含具体问题。给出问题文本后即可作答；问题内容无法自行补齐。

## B201（语气与防御）

输入：回答一个通用问题

负例描述：求助式结尾

输出：具体问题未随消息给出。请提供待回答的内容本身；若问题涉及 DSH（运行中安装的版本），需指明具体模块或文件，以便查阅文档与源码后作答。

## B202（语气与防御）

输入：回答一个通用问题

负例描述：询问式收尾

输出：消息中只有「回答一个通用问题」一句，问题文本未出现。该文本不在任何配置文件、源码或文档中，无法自行补齐。给出具体问题内容后即可作答。

## B203（语气与防御）

输入：回答一个通用问题

负例描述：过度承诺服务

输出：消息中未包含具体题目。作答需要题目本身或待答文本；当前只有一个说明性句子，缺少可回答的内容。补上题目即可。

## B204（语气与防御）

输入：回答一个通用问题

负例描述：免责声明

输出：消息中没有具体问题，只有「回答一个通用问题」这一句。问题对象缺失，无法自行补齐，因为可回答的内容取决于所问的具体事项。

补充问题本身即可，任何领域均可。

## B205（语气与防御）

输入：回答一个通用问题

负例描述：价值判断模糊

输出：消息中只有「回答一个通用问题」这一句说明，未附具体问题内容。可回答的对象缺失，无法自行补齐：通用问题的范围不构成可判定的题目。

请给出具体问题文本。若问题涉及 DSH，请说明所指版本或模块；本机安装文档与源码可直接查阅后作答。

## B206（语气与防御）

输入：回答一个通用问题

负例描述：回避正面

输出：本轮消息未包含待答的问题内容，缺的是问题原文本身。补充问题原文后按该问题作答。

## B207（语气与防御）

输入：回答一个通用问题

负例描述：万能建议

输出：缺少待回答的具体问题。请给出问题内容。

## B208（句式与结构）

输入：回答一个通用问题

负例描述：情绪化强调

输出：未提供需要回答的问题内容。本轮消息只说明了「回答一个通用问题」这一要求，未给出问题对象，无法自行补齐。请给出具体问题。

## B209（句式与结构）

输入：回答一个通用问题

负例描述：命令式建议

输出：本轮消息未给出待回答的问题内容，缺少回答对象。补上具体问题即可开始。

## B210（语气与防御）

输入：回答一个通用问题

负例描述：过度共情

输出：消息中未包含待回答的问题本身，只有「回答一个通用问题」这一指令。通用问题不指向任何具体对象，无法确定答题范围与所需的答案形态。

需要给出具体问题文本，或指定领域与题面。
