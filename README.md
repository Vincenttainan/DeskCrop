# DeskCrop  
---  
## [v0.0](https://github.com/Vincenttainan/DeskCrop/tree/e90e795b43aa4cfe0273bcc9bf0b837b3711f2e8)  

<details>

### 簡介  
DeskCrop 是一個小型懸浮視窗範例，永遠置於桌面最上方，目前僅包含 Mac 風格關閉按鈕  

### 功能  
* 懸浮視窗，始終在最上層  
* 自訂紅色圓形關閉按鈕  
    * 滑鼠移入顯示黑色叉叉  
    * 點擊關閉視窗

### 執行方式  
```bash
python DeskCrop.py
```

### 專案結構  
```
DeskCrop/
├── ui/
│   ├── Buttons.py       # Mac 風格關閉按鈕元件
│   └── __init__.py
├── DeskCrop.py          # 主程式
├── game/                # 後續遊戲邏輯
├── data/                # 後續存檔或設定
└── assets/              # 後續圖片、素材
```

### 未來規劃  
* 多塊土地的桌面種田遊戲  
* 自動收成 / 掛機功能  
* 作物品質系統與升級系統  
* UI 改進動畫效果

</details>  

---

## [v0.1](https://github.com/Vincenttainan/DeskCrop/tree/2c85b24bc3991132ddbf5271fe63d091e7d7e5b7)  

<details>

### 簡介  
新增一塊土地可種植與收穫，體驗基本掛機互動  

### 功能  
* v0.0 功能
* 單塊土地  
    * 空地 → 褐色  
    * 生長中 → 綠色  
    * 成熟 → 黃色  
* 滑鼠移過土地 → 種植/收成  

### 專案結構  
```
DeskCrop/
├── ui/
│   ├── tile_view.py     # 可視化的遊戲邏輯
│   ├── Buttons.py       # Mac 風格關閉按鈕元件
│   └── __init__.py
├── game/
│   └── tile.py          # 遊戲邏輯
├── DeskCrop.py          # 主程式
├── data/                # 後續存檔或設定
└── assets/              # 後續圖片、素材
```

### 未來規劃  
* 多塊土地管理    
* 自動收成 / 掛機功能  
* 作物品質系統與升級系統  
* UI 改進動畫效果  

</details>

---

## [v0.2](https://github.com/Vincenttainan/DeskCrop/tree/f2511598d5ed4a14d15dc2c27114851e5fe87650)  

<details>

### 簡介  
可新增一大片土地可種植與收穫，體驗基本掛機互動  
加入 money 系統  

### 功能  
* v0.1 功能
* 多塊土地  
* 成熟作物收成時增加金錢  

### 專案結構  
```
DeskCrop/
├── ui/
│   ├── Buttons.py       # Mac 風格關閉按鈕元件
│   ├── TileView.py      # 土地視覺與互動
│   ├── MoneyView.py     # 顯示金錢的 Label
│   ├── FarmView.py      # 整合處理 Tile
│   └── __init__.py
├── game/
│   ├── tile.py          # 土地 / 作物邏輯
│   └── Money.py         # 金錢邏輯
├── DeskCrop.py          # 主程式
├── data/                # 後續存檔或設定
└── assets/              # 後續圖片、素材
```

### 未來規劃  
* 自動收成 / 掛機功能
* 作物品質系統與升級系統  
* 多塊土地的擴充與布局優化  
* UI 改進動畫效果  

</details>

---

## [v0.3](https://github.com/Vincenttainan/DeskCrop/tree/f231e9bac9be43b29ee2e44d29b914334ec211ee)  

<details>

### 簡介  
完成核心遊戲循環，加入存檔 / 讀檔機制  
關閉程式後作物仍會持續生長，重新開啟可正確恢復狀態  

### 功能  
* v0.2 所有功能  
* 存檔 / 讀檔系統（JSON）  
* 土地狀態保存（EMPTY / GROWING / READY）  
* 作物生長時間保存（支援離線成長）  
* 金錢數值保存與恢復  

### 專案結構  
```
DeskCrop/
├── data/
│   ├── SaveLoadManager.py     # 存檔讀檔處理
│   └── save.json              # 可有可無，反正就存遊戲進度
├── ui/
│   ├── Buttons.py             # Mac 風格關閉按鈕元件
│   ├── TileView.py            # 土地視覺與互動
│   ├── MoneyView.py           # 顯示金錢的 Label
│   ├── FarmView.py            # 整合處理 Tile
│   └── __init__.py
├── game/
│   ├── tile.py                # 土地 / 作物邏輯
│   └── Money.py               # 金錢邏輯
├── DeskCrop.py                # 主程式
└── assets/                    # 後續圖片、素材
```

### 未來規劃  

* 自動收成  
* 作物品質系統與升級系統  
* 土地解鎖（lock / unlock）系統  
* 作物種類與成長差異  
* 升級與花費金錢機制  
* 更完整的 UI 與動畫效果  

</details>
