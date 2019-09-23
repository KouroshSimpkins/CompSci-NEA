//
//  CameraController.swift
//  CompSciNEA
//
//  Created by Kourosh Simpkins on 23/09/2019.
//  Copyright © 2019 Kourosh Simpkins. All rights reserved.
//

import AVFoundation

class CameraController {
    func prepare(completionHandler: @escaping (Error?) -> Void) {
        func createCaptureSession() {self.captureSession = AVCaptureSession() }
        func configureCaptureDevices() throws { }
        func configureDeviceInputs() throws { }
        func configurePhotoOutput() throws { }
        
        DispatchQueue(label: "prepare").async {
            do {
                createCaptureSession()
                try configureCaptureDevices()
                try configureDeviceInputs()
                try configurePhotoOutput()
            }
            
            catch {
                DispatchQueue.main.async {
                    completionHandler(error)
                }
                
                return
            }
            
            DispatchQueue.main.async {
                completionHandler(nil)
            }
        }
    }
}

var captureSession: AVCaptureSession?
